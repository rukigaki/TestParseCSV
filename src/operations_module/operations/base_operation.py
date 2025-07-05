from abc import ABC, abstractmethod


class NegativePriceError(Exception):
    pass


class BaseOperation(ABC):

    @abstractmethod
    def operation_on_table(self, table_data):
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


