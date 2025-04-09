import csv
import pandas as pd


def csv_open(path: str) -> list[dict]:
    csv_transactions = []
    with open(path, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)
        for row in reader:
            csv_transaction = dict(zip(headers, row))
            csv_transactions.append(csv_transaction)
        return csv_transactions


def xlsx_open(file_path):
    try:
        df = pd.read_excel(file_path, sheet_name="Sheet1", dtype=str)
        return df.to_dict("records")
    except FileNotFoundError:
        return []
