"""
DART disclosure data collector.

This file will collect corporate disclosure data from DART
and save it into the data/raw directory.
"""

from datetime import datetime


def main():
    today = datetime.today().strftime("%Y-%m-%d")
    print("DART collector is ready.")
    print(f"Today: {today}")


if __name__ == "__main__":
    main()
