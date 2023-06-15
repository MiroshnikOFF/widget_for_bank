import json
from src.operation import Operation
import datetime


def get_operations_list(operations):
    """
    Получает json файл операций, возвращает список словарей операций
    :param operations: json
    :return: list
    """
    with open(operations, 'r') as file:
        operations_list = json.load(file)
        return operations_list


def get_operations_class_list(operations_list):
    """
    Преобразует список операций в список объектов класса Operation
    :param operations_list: список операций
    :return: список объектов класса Operation
    """
    operations_class_list = []
    for operation in operations_list:
        if "id" in operation:
            num = operation["id"]
        else:
            num = "-"
        if "state" in operation:
            state = operation["state"]
        else:
            state = "-"
        if "date" in operation:
            date = operation["date"]
        else:
            date = "-"
        if "operationAmount" in operation:
            amount = operation["operationAmount"]
        else:
            amount = "-"
        if "description" in operation:
            description = operation["description"]
        else:
            description = "-"
        if "from" in operation:
            out = operation["from"]
        else:
            out = "-"
        if "to" in operation:
            to = operation["to"]
        else:
            to = "-"
        operation = Operation(num, state, date, description, out, to, amount)
        operations_class_list.append(operation)
    return operations_class_list


def operations_sorted(objects_list):
    """
    Сортирует операции по дате по убыванию
    :param objects_list: список объектов класса Operation
    :return: отсортированный список объектов класса Operation
    """
    objects_for_sort = {}
    operations_sorted_done = []
    # Создает словарь для сортировки
    for obj in objects_list:
        if obj.state == "EXECUTED":
            # Отбрасывает время и преобразует в объект datetime
            date_without_time = obj.date.split("T")[0]
            date = datetime.datetime.strptime(date_without_time, "%Y-%m-%d")
            # Добавляет в словарь пару int(дата): <операция>
            objects_for_sort[date] = obj
    # Сортирует словарь по дате
    objects_sorted = dict(sorted(objects_for_sort.items()))
    # Разворачивает словарь
    objects_reversed = dict(reversed(objects_sorted.items()))
    # Создает список отсортированных <операций>
    for value in objects_reversed.values():
        operations_sorted_done.append(value)
    return operations_sorted_done






