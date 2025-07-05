from .constants import ComparisonEnum
from src.operations_module.operations.base_operation import BaseOperation


class FilterOperation(BaseOperation):

    def __init__(self, args):
        self.where = args.where

    def operation_on_table(self, table_data: list[dict]) -> list:
        """
        см. -> base_operation.operation_on_table
        """

        for operator_set in ComparisonEnum:
            operator_str, operator_func = operator_set.value
            if operator_str in self.where:
                column, value = self.where.split(operator_str)

                table_data = [row for row in table_data
                              if operator_func(self.simple_validation(row[column]),
                                                self.simple_validation(value))]
                return table_data

        raise ValueError("Отсутствует оператор сравнения!")