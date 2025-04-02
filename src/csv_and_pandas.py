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


def xlsx_open(path: str) -> list[dict]:
    excel_data = pd.read_excel(path)
    xlsx_transactions = excel_data.to_dict()
    xlsx_transactions = excel_data.to_dict(orient="records")
    return xlsx_transactions
