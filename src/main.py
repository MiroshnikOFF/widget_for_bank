from src.utils import get_operations_list, get_operations_class_list, operations_sorted

# json файл с данными об операциях
operations_json = "operations.json"

# Распаковка данных об операциях из json в список словарей
operations_list = get_operations_list(operations_json)

# Преобразование списка словарей в список экземпляров класса Operation
operations_objects = get_operations_class_list(operations_list)

# Сортировка списка экземпляров класса Operation
operations_sorted = operations_sorted(operations_objects)

# Подготовка списка для вывода
operations_for_print = operations_sorted[:3]

# Вывод трех последних операций
for operation in operations_for_print:
    print(operation)
