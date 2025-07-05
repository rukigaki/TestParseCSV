from .constants import AggregateEnum
from src.operations_module.operations.base_operation import BaseOperation


class AggregateOperation(BaseOperation):

    def __init__(self, args):
        self.aggregate = args.aggregate


    def operation_on_table(self, table_data: list[dict]) -> list[dict]:
        """
        см. -> base_operation.operation_on_table
        """

        column, method_aggregate_str = self.aggregate.split("=")
        values = map(lambda x: self.simple_validation(x[column]), table_data)

        for aggr_set in AggregateEnum:
            method_aggr_str_enum, method_aggr_enum = aggr_set.value

            if method_aggr_str_enum == method_aggregate_str:
                result = method_aggr_enum(values)

                if method_aggregate_str == AggregateEnum.AVG.value[0]:
                    result /= len(table_data)

                table_data = [{method_aggr_str_enum: result}]

                return table_data

        raise ValueError("Введите одну из функций агрегации: max, min, avg")