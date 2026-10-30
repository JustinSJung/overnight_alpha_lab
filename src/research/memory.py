"""Small immutable hash-linked research events, including failures and reservations."""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path

from src.research.programs import canonical

MAX_EVENT_BYTES = 40_000
MAX_EVENTS = 500


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def read_memory(root):
    root = Path(root)
    if root.is_symlink():
        raise ValueError('Research memory must not be a symlink.')
    paths = sorted(root.glob('event_*.json'))
    if len(paths) > MAX_EVENTS:
        raise ValueError('Research memory capacity requires review.')
    events, previous = [], '0' * 64
    for index, path in enumerate(paths):
        if path.is_symlink() or path.stat().st_size > MAX_EVENT_BYTES:
            raise ValueError('Unsafe research event file.')
        event = json.loads(path.read_text())
        if (path.name != f'event_{index:06d}.json' or set(event) != {'sequence', 'previous', 'at', 'kind', 'payload', 'sha256'}
                or event['sequence'] != index or event['previous'] != previous
                or event['sha256'] != digest({key: value for key, value in event.items() if key != 'sha256'})):
            raise ValueError('Research history was changed or lost; do not reset it.')
        events.append(event)
        previous = event['sha256']
    head = root / 'head.json'
    if head.exists() or head.is_symlink():
        if head.is_symlink() or head.stat().st_size > 1000:
            raise ValueError('Unsafe research memory head.')
        anchor = json.loads(head.read_text())
        if anchor != {'count': len(events), 'sha256': previous}:
            raise ValueError('Research event tail is missing or incomplete.')
    elif events:
        raise ValueError('Research memory head is missing.')
    return events


@contextmanager
def locked_memory(root):
    root = Path(root)
    if root.is_symlink():
        raise ValueError('Research memory must not be a symlink.')
    root.mkdir(parents=True, exist_ok=True)
    lock = root / '.lock'
    if lock.is_symlink():
        raise ValueError('Unsafe research lock.')
    with lock.open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield read_memory(root)
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def append_event(root, events, kind, payload):
    if len(events) >= MAX_EVENTS:
        raise ValueError('Research memory is full; review is required.')
    event = dict(sequence=len(events), previous=events[-1]['sha256'] if events else '0' * 64,
                 at=datetime.now(timezone.utc).isoformat(), kind=kind, payload=payload)
    event['sha256'] = digest(event)
    content = canonical(event) + '\n'
    if len(content.encode()) > MAX_EVENT_BYTES:
        raise ValueError('Research event exceeds its size budget.')
    path = Path(root) / f'event_{len(events):06d}.json'
    with path.open('x', encoding='utf-8') as handle:
        handle.write(content)
        handle.flush()
    head = Path(root) / 'head.json'
    temporary = Path(root) / '.head.tmp'
    if head.is_symlink() or temporary.is_symlink():
        raise ValueError('Unsafe research memory head.')
    temporary.write_text(canonical({'count': len(events) + 1, 'sha256': event['sha256']}) + '\n')
    temporary.replace(head)
    events.append(event)
    return event
