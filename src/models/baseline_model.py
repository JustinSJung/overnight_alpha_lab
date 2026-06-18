import os
from datetime import datetime

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


NUMERIC_FEATURES = [
    "event_score",
    "news_count",
    "positive_keyword_count",
    "negative_keyword_count",
    "news_sentiment_score",
    "news_attention_score",
]

CATEGORICAL_FEATURES = [
    "event_type",
    "prediction_direction",
    "initial_confidence",
]

TARGET_COLUMN = "prediction_result"


def get_latest_ml_dataset():
    processed_dir = "data/processed"

    files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("ml_dataset_") and file.endswith(".csv")
    ]

    if not files:
        raise FileNotFoundError("No ml_dataset CSV file found.")

    files.sort(reverse=True)
    return os.path.join(processed_dir, files[0])


def load_dataset(path):
    df = pd.read_csv(path)

    if TARGET_COLUMN not in df.columns:
        raise ValueError("prediction_result column not found.")

    train_df = df[df[TARGET_COLUMN].isin(["success", "failure"])].copy()

    return df, train_df


def build_model(numeric_features, categorical_features):
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value=0)),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="unknown")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    return model


def save_report(lines):
    output_dir = "reports/daily_review"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(output_dir, today + "_baseline_model_report.md")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return output_path


def main():
    print("Training baseline machine learning model...")

    dataset_path = get_latest_ml_dataset()
    print("ML dataset file:", dataset_path)

    df, train_df = load_dataset(dataset_path)

    total_rows = len(df)
    trainable_rows = len(train_df)

    print("Total dataset rows:", total_rows)
    print("Trainable rows:", trainable_rows)

    report_lines = []
    report_lines.append("# Baseline Model Report")
    report_lines.append("")
    report_lines.append("## Dataset Summary")
    report_lines.append("")
    report_lines.append("- Total rows: " + str(total_rows))
    report_lines.append("- Trainable rows: " + str(trainable_rows))
    report_lines.append("")

    if trainable_rows < 10:
        report_lines.append("## Status")
        report_lines.append("")
        report_lines.append("Not enough trainable samples yet.")
        report_lines.append("")
        report_lines.append("Most rows are still pending because next trading day price data is not available yet.")

        output_path = save_report(report_lines)

        print("Not enough trainable samples yet.")
        print("Report saved to:", output_path)
        return

    available_numeric = [col for col in NUMERIC_FEATURES if col in train_df.columns]
    available_categorical = [col for col in CATEGORICAL_FEATURES if col in train_df.columns]

    feature_columns = available_numeric + available_categorical

    X = train_df[feature_columns].copy()
    y = train_df[TARGET_COLUMN].map({"failure": 0, "success": 1})

    if y.nunique() < 2:
        report_lines.append("## Status")
        report_lines.append("")
        report_lines.append("Not enough class diversity.")
        report_lines.append("")
        report_lines.append("A model needs both success and failure samples.")

        output_path = save_report(report_lines)

        print("Not enough class diversity.")
        print("Report saved to:", output_path)
        return

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y,
    )

    model = build_model(available_numeric, available_categorical)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    report_lines.append("## Status")
    report_lines.append("")
    report_lines.append("Baseline model trained successfully.")
    report_lines.append("")
    report_lines.append("## Features")
    report_lines.append("")
    report_lines.append("- Numeric features: " + str(available_numeric))
    report_lines.append("- Categorical features: " + str(available_categorical))
    report_lines.append("")
    report_lines.append("## Accuracy")
    report_lines.append("")
    report_lines.append(str(round(accuracy, 4)))
    report_lines.append("")
    report_lines.append("## Classification Report")
    report_lines.append("")
    report_lines.append("```text")
    report_lines.append(class_report)
    report_lines.append("```")

    output_path = save_report(report_lines)

    print("Accuracy:", round(accuracy, 4))
    print(class_report)
    print("Report saved to:", output_path)


if __name__ == "__main__":
    main()
