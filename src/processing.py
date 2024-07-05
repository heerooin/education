from typing import Any

just_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(just_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция сортировки по стэйту"""
    finish_list = []
    for i in just_list:
        if i.get("state") == state:
            finish_list.append(i)
    return finish_list


def sort_by_date(just_list: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки по дате"""
    sorted_just_list=sorted(just_list, key=lambda just_list: just_list["date"], reverse = reverse)
    return  sorted_just_list
