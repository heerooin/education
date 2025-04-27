import re


def bank_operations(list_operations: dict , search: str) -> list[dict] :
    """Функция для поиска по строки"""
    operations = []
    pattern = re.compile(search, re.IGNORECASE)
    for operation in list_operations:
        if "description" in operation and pattern.search(operation["description"]):
            operations.append(operation)
    return operations


def category_operations(transactions_list: dict, count_dict: dict = None) -> dict:
    """Подсчета операций"""
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
