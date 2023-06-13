import pytest
from src import utils
import json


@pytest.fixture
def operations_list():
    return [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            }
           ]


def test_get_operations_list(operations_list):
    with open('temp.json', 'w',) as file:
        json.dump(operations_list, file)
    result = utils.get_operations_list('temp.json')
    assert result == operations_list


@pytest.mark.parametrize("operation, expected", [
    ([{"id": "Ok", "state": "Ok", "date": "Ok",
       "description": "Ok", "from": "Ok", "to": "Ok"}], "Ok"),
    ([{}], "-")
])
def test_get_operations_class_list(operation, expected):
    operation_class_list = utils.get_operations_class_list(operation)
    assert operation_class_list[0].num == expected
    assert operation_class_list[0].state == expected
    assert operation_class_list[0].date == expected
    assert operation_class_list[0].description == expected
    assert operation_class_list[0].out == expected
    assert operation_class_list[0].to == expected


def test_operations_sorted(operations_list):
    obj_list = utils.get_operations_class_list(operations_list)
    sort_list = utils.operations_sorted(obj_list)
    dates = []
    for el in sort_list:
        date = el.date.split("T")[0]
        clear_data = "".join(date.split("-"))
        dates.append(clear_data)
    date_1 = 0
    date_2 = 1
    for el in range(len(dates) - 1):
        assert dates[date_1] > dates[date_2]
        date_1 += 1
        date_2 += 1



