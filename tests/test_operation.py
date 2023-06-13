import pytest
from src.utils import get_operations_class_list


@pytest.mark.parametrize("key, date, expected", [
    ("date", "2019-08-26T10:50:58.294041", "26.08.2019")
])
def test_get_date(key, date, expected):
    obj_date = get_operations_class_list([{key: date}])
    assert obj_date[0].get_date() == expected


@pytest.mark.parametrize("key, out, expected", [
    ("from", "Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("from", "-", "cash")
])
def test_mask_from(key, out, expected):
    obj_out = get_operations_class_list([{key: out}])
    assert obj_out[0].mask_from() == expected


@pytest.mark.parametrize("key, to, expected", [
    ("to", "Счет 64686473678894779589", "Счет ****9589"),
    ("to", "-", "cash")
])
def test_mask_to(key, to, expected):
    obj_out = get_operations_class_list([{key: to}])
    assert obj_out[0].mask_to() == expected

