"""Bounded numerical programs, interpreted as data rather than executable Python."""
from __future__ import annotations

import hashlib
import json

import numpy as np

from src.features.next_open_dataset import COLUMNS

UNARY = ('abs', 'tanh', 'signed_log')
BINARY = ('add', 'subtract', 'multiply', 'safe_divide', 'minimum', 'maximum')
OPERATIONS = UNARY + BINARY
MAX_NODES = 8


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def validate_program(program):
    if (not isinstance(program, dict) or set(program) != {'schema', 'learner', 'nodes', 'outputs'}
            or program['schema'] != 'numerical_research_program_v1'
            or program['learner'] not in ('linear', 'hgb_shallow')):
        raise ValueError('Unsupported research program.')
    nodes, outputs = program['nodes'], program['outputs']
    if (not isinstance(nodes, list) or not 1 <= len(nodes) <= MAX_NODES
            or not isinstance(outputs, list) or not 1 <= len(outputs) <= 4
            or any(type(i) is not int or not 0 <= i < len(nodes) for i in outputs)
            or len(set(outputs)) != len(outputs)):
        raise ValueError('Invalid program size or outputs.')
    for i, node in enumerate(nodes):
        if not isinstance(node, dict) or set(node) != {'op', 'inputs'} or node['op'] not in OPERATIONS:
            raise ValueError('Only numerical operations are permitted.')
        refs = node['inputs']
        if not isinstance(refs, list) or len(refs) != (1 if node['op'] in UNARY else 2):
            raise ValueError('Wrong numerical operation arity.')
        for ref in refs:
            if not ((isinstance(ref, str) and ref in COLUMNS) or (type(ref) is int and 0 <= ref < i)):
                raise ValueError('Only completed input features and preceding nodes are accessible.')
    return program


def program_id(program):
    validate_program(program)
    return hashlib.sha256(canonical(program).encode()).hexdigest()


def transform(program, frame):
    """Pointwise only: no labels, row shifts, date joins, file access or code execution."""
    validate_program(program)
    raw = frame[COLUMNS].to_numpy(dtype=float)
    if not np.isfinite(raw).all():
        raise ValueError('Finite completed input features are required.')
    features = {name: np.clip(raw[:, i], -20., 20.) for i, name in enumerate(COLUMNS)}
    values = []
    for node in program['nodes']:
        args = [features[ref] if isinstance(ref, str) else values[ref] for ref in node['inputs']]
        op, a = node['op'], args[0]
        if op == 'abs':
            value = np.abs(a)
        elif op == 'tanh':
            value = np.tanh(a)
        elif op == 'signed_log':
            value = np.sign(a) * np.log1p(np.abs(a))
        else:
            b = args[1]
            if op == 'add': value = a + b
            elif op == 'subtract': value = a - b
            elif op == 'multiply': value = a * b
            elif op == 'minimum': value = np.minimum(a, b)
            elif op == 'maximum': value = np.maximum(a, b)
            else:
                denominator = np.where(np.abs(b) < .05, np.where(b < 0, -.05, .05), b)
                value = a / denominator
        values.append(np.clip(value, -20., 20.))
    result = np.column_stack([raw] + [values[i] for i in program['outputs']])
    if not np.isfinite(result).all():
        raise ValueError('Invalid research feature output.')
    return result


def propose(memory, seed):
    """Remember all attempted programs; prefer ranked parents but keep exploration."""
    rng = np.random.default_rng(seed)
    trials = [event['payload'] for event in memory if event['kind'] == 'trial']
    seen = {event['payload']['program_id'] for event in memory
            if event['kind'] in ('proposal', 'trial')}
    parents = sorted([row for row in trials[-20:] if row['status'] == 'completed'],
                     key=lambda row: (-row['metrics']['development_brier_improvement'], row['program_id']))[:5]
    for _ in range(100):
        parent = parents[int(rng.integers(len(parents)))] if parents and rng.random() < .7 else None
        if parent:
            candidate = json.loads(canonical(parent['program']))
            index = int(rng.integers(len(candidate['nodes'])))
            op = str(rng.choice(OPERATIONS))
            refs = COLUMNS + list(range(index))
            candidate['nodes'][index] = {'op': op, 'inputs': [refs[int(rng.integers(len(refs)))]
                                                            for _ in range(1 if op in UNARY else 2)]}
        else:
            nodes = []
            for index in range(int(rng.integers(2, 6))):
                op = str(rng.choice(OPERATIONS))
                refs = COLUMNS + list(range(index))
                nodes.append({'op': op, 'inputs': [refs[int(rng.integers(len(refs)))]
                                                   for _ in range(1 if op in UNARY else 2)]})
            candidate = dict(schema='numerical_research_program_v1', learner=str(rng.choice(['linear', 'hgb_shallow'])),
                             nodes=nodes, outputs=list(range(max(0, len(nodes) - 3), len(nodes))))
        if program_id(candidate) not in seen:
            return candidate, parent['program_id'] if parent else None
    raise ValueError('Novel program search exhausted its bounded attempt budget.')
