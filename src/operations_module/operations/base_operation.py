from abc import ABC, abstractmethod


class NegativePriceError(Exception):
    pass


class BaseOperation(ABC):

    @abstractmethod
    def operation_on_table(self, table_data):
        """
        Абстрактный метод для создания Операций, которые будут применены для манипуляции с таблицей
        Example: aggregate, order_by, sorting и т.д.

        :param table_data: Это распарсенный csv-файл, который является списком словарей
        Example: [{"brand": "apple", "price": "100", "rating": "4.5"},
                {"brand": "samsung", "price": "200", "rating": "3.5"}]


        :return: Возвращает уже готовый объект в orchestrator.py, который вызывается в main.py(точка входа)
        """
        pass


    @staticmethod
    def simple_validation(value) -> int | float | str:
        for cast in (int, float):
            try:
                validated_value = cast(value)
                if validated_value < 0:
                    raise NegativePriceError("Это отрицательное число!")
                return validated_value
            except ValueError:
                continue
        return value


