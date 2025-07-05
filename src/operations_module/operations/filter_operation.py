from src.operations_module.operations.constants import OPERATORS
from src.operations_module.operations.base_operation import BaseOperation


class FilterOperation(BaseOperation):

    def __init__(self, args):
        self.where = args.where

    def operation_on_table(self, table_data: list[dict]) -> list:
        for operator_key in OPERATORS:
            if operator_key in self.where:
                column, value = self.where.split(operator_key)
                operator_func = OPERATORS[operator_key]

                table_data = [row for row in table_data
                              if operator_func(self.simple_validation(row[column]),
                                                self.simple_validation(value))]
                return table_data

        raise ValueError("Отсутствует оператор сравнения!")