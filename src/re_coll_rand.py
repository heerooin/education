import re
import json
from src.utils import open_file
from collections import Counter
from src.csv_and_pandas import csv_open, xlsx_open
from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_data, mask_account_card
from src.processing import sort_by_date
from src.generators import filter_by_currency


def bank_operations(list_operations: dict , search: str) -> list[dict] :
    operations = []
    pattern = re.compile(search, re.IGNORECASE)
    for operation in list_operations:
        if "description" in operation and pattern.search(operation["description"]):
            operations.append(operation)
    return operations


def category_operations(transactions_list: dict, count_dict: dict = None) -> dict:
    descriptions = []
    for operation in transactions_list:
        if "description" in operation:
            descriptions.append(operation["description"])
    counted = Counter(descriptions)

    if count_dict is not None:
        result = count_dict.copy()
        for key, value in counted.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
        return result
    return dict(counted)


def main():
    """Основная функция пользовательского интерфейса"""
    result = []
    final_result = []
    value = ('EXECUTED', 'CANCELED', 'PENDING')
    print("Привет! Добро пожаловать в программу работы\n"
          "с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла\n")
    possible_types = {1: "JSON",
                      2: "CSV",
                      3: "XLSX"}
    file_type = int(input())
    if file_type in possible_types:
        file_type = possible_types[file_type]
        if file_type == "JSON":
            final = (open_file("../data/operations.json"))
        elif file_type == "CSV":
            final = csv_open("../data/transactions.csv")
        else:
            final = xlsx_open("../data/transactions_excel.xlsx")

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
        status = input()
        if status.upper() in value:
            status = status.upper()
            result = []
            for i in final:
                if 'state' in i:
                    if i['state'] == status:
                        result.append(i)
            print(f"\nОперации отфильтрованы по статусу {status}")
            break
        else:
            print(f"\nСтатус операции {status} недоступен.")

    print("\nОтсортировать операции по дате? Да/Нет\n")
    date = input()
    if date.capitalize() == 'Да':
        result = sort_by_date(result)

    print("\nОтсортировать По возрастанию или По убыванию?\n")
    sort = input()
    if sort.capitalize() == 'по возрастанию':
        sort = True
    else:
        sort = False

    print("\nВыводить только рублевые тразакции? Да/Нет\n")
    rub = input()
    if rub.capitalize() == 'Да':
        total = len(result)
        result = filter_by_currency(result, "RUB")
        for _ in range(total):
            try:
                final_result.append(next(result))
            except StopIteration:
                break

    print("\nОтфильтровать список транзакций по определенному слову "
          "в описании? Да/Нет\n")
    discr = input()
    if discr.capitalize() == 'Да':
        print('Введите слово для поиска:\n')
        search = input()
        if final_result:
            final_result = bank_operations(final_result, search)
        else:
            print("Нет операций для фильтрации")

    print("\nРаспечатываю итоговый список транзакций...\n")
    if final_result:
        print(f'Всего банковских операций в выборке: {len(final_result)}')
        for i in final_result:
            if "date" in i and "description" in i:
                print(f'{get_data(i["date"])} {i["description"]}')

                if "from" in i and "to" in i:
                    if i["description"] == "Перевод со счета на счет":
                        from_account = mask_account_card(i["from"])
                        to_account = mask_account_card(i["to"])
                        print(f'{from_account} -> {to_account}')
                    elif i["description"] == "Перевод с карты на карту":
                        from_card = mask_account_card(i["from"])
                        to_card = mask_account_card(i["to"])
                        print(f'{from_card} -> {to_card}')
                    elif i["description"] == "Перевод организации":
                        from_account = mask_account_card(i["from"])
                        to_account = mask_account_card(i["to"])
                        print(f'{from_account} -> {to_account}')
                elif i["description"] == "Открытие вклада" and "to" in i:
                    print(f'Счет {get_mask_account(i["to"][5:])}')

                if "operationAmount" in i:
                    amount = i["operationAmount"]["amount"]
                    currency_name = i["operationAmount"]["currency"]["name"]
                    print(f'Сумма: {amount} {currency_name}')
                print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши\n"
              "условия фильтрации")


if __name__ == '__main__':
    main()
