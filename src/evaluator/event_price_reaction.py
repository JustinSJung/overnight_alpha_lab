"""
Event-price reaction evaluator.

This script connects parsed DART disclosure events
with stock price data and calculates simple next-day reactions.
"""

import os

import pandas as pd


def normalize_stock_code(value) -> str:
    """
    Normalize stock code to 6-digit string.
    """

    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except ValueError:
        return str(value).strip().zfill(6)


def get_latest_processed_dart_file(processed_dir: str = "data/processed") -> str:
    """
    Find the latest parsed DART disclosure CSV file.
    """

    csv_files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("parsed_dart_disclosures_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No parsed DART disclosure CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(processed_dir, csv_files[0])


def get_latest_price_file(stock_code: str, raw_dir: str = "data/raw") -> str:
    """
    Find the latest price CSV file for a stock code.
    """

    csv_files = [
        file for file in os.listdir(raw_dir)
        if file.startswith(f"price_{stock_code}_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError(f"No price CSV files found for stock_code={stock_code}.")

    csv_files.sort(reverse=True)
    return os.path.join(raw_dir, csv_files[0])


def calculate_next_day_reaction(event_date: str, price_df: pd.DataFrame) -> dict:
    """
    Calculate next available trading day's opening and closing reaction.
    """

    price_df = price_df.copy()
    price_df["date"] = pd.to_datetime(price_df["date"])
    event_datetime = pd.to_datetime(str(event_date))

    previous_prices = price_df[price_df["date"] <= event_datetime].sort_values("date")
    future_prices = price_df[price_df["date"] > event_datetime].sort_values("date")

    if previous_prices.empty or future_prices.empty:
        return {
            "next_trade_date": None,
            "next_open_return": None,
            "next_close_return": None,
            "note": "No next trading day price data available yet.",
        }

    base_close = previous_prices.iloc[-1]["close"]
    next_day = future_prices.iloc[0]

    next_open_return = (next_day["open"] - base_close) / base_close
    next_close_return = (next_day["close"] - base_close) / base_close

    return {
        "next_trade_date": next_day["date"].strftime("%Y-%m-%d"),
        "next_open_return": round(next_open_return, 4),
        "next_close_return": round(next_close_return, 4),
        "note": "",
    }


def evaluate_stock_events(stock_code: str) -> pd.DataFrame:
    """
    Evaluate DART events for a single stock code.
    """

    stock_code = normalize_stock_code(stock_code)

    dart_file = get_latest_processed_dart_file()
    price_file = get_latest_price_file(stock_code)

    print(f"DART file: {dart_file}")
    print(f"Price file: {price_file}")

    dart_df = pd.read_csv(dart_file)
    price_df = pd.read_csv(price_file)

    dart_df["normalized_stock_code"] = dart_df["stock_code"].apply(normalize_stock_code)

    print()
    print("Available stock codes in latest DART file:")
    print(
        dart_df[["corp_name", "normalized_stock_code", "report_nm", "event_type"]]
        .head(30)
        .to_string(index=False)
    )
    print()

    stock_events = dart_df[dart_df["normalized_stock_code"] == stock_code].copy()

    if stock_events.empty:
        print(f"No DART events found for stock_code={stock_code}.")
        print("Try one of the stock codes shown above.")
        return pd.DataFrame()

    results = []

    for _, event in stock_events.iterrows():
        event_date = str(event["rcept_dt"])

        reaction = calculate_next_day_reaction(event_date, price_df)

        results.append(
            {
                "stock_code": stock_code,
                "corp_name": event.get("corp_name", ""),
                "report_nm": event.get("report_nm", ""),
                "event_type": event.get("event_type", ""),
                "event_date": event_date,
                "next_trade_date": reaction["next_trade_date"],
                "next_open_return": reaction["next_open_return"],
                "next_close_return": reaction["next_close_return"],
                "note": reaction["note"],
            }
        )

    return pd.DataFrame(results)


def save_evaluation_result(df: pd.DataFrame, stock_code: str) -> str:
    """
    Save event-price reaction result.
    """

    output_dir = "data/predictions"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/event_price_reaction_{stock_code}.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    stock_code = "267260"

    print(f"Evaluating event-price reactions for {stock_code}...")

    result_df = evaluate_stock_events(stock_code)

    if result_df.empty:
        print("No evaluation result saved.")
        return

    output_path = save_evaluation_result(result_df, stock_code)

    print(f"Saved result to: {output_path}")
    print()
    print(result_df.to_string(index=False))


if __name__ == "__main__":
    main()
