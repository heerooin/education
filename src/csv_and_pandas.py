import csv
import pandas as pd


def csv_open(path: str) -> list[dict]:
    with open(path) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for row in reader:
            print(row)


def xlsx_open(path: str) -> list[dict]:
    excel_data = pd.read_excel(path)
    return excel_data
