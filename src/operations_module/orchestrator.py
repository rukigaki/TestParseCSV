from .operations import *



class Operations:
    """
    Класс Оркестратор, который собирает все логику вызовов методов манипулирования таблицей
    Example: aggregate, order_by, sorting и т.д.

    __call__ - магический метод, который автоматизирует всю логику вызовов функций см. Example выше.

    Пример команды где извлекаются аргументы file where order_by. Вся верхнеуровневая логика содержится в этом классе
    Example: python main.py --file src/products.csv --where "brand=apple" --order_by "price=asc".

    Таким образом не нужно думать в каком порядке и что с чем можно вызывать, об этом думает функция __cal__.
    Если требуется изменить логику вам туда.
    """

    __slots__ = ("_methods", "args", "arguments")

    def __init__(self, arg) -> None:
        self.args = arg
        self.arguments = [arg.where, arg.order_by, arg.aggregate]

        self._methods = [
            FilterOperation(self.args),
            OrderByOperation(self.args),
            AggregateOperation(self.args),
        ]


    def __call__(self, table_data) -> list:
        table = table_data
        for ind, method in enumerate(self.arguments):
            if method is None:
                continue

            table = self._methods[ind].operation_on_table(table)


        return table