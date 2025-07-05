from src.operations_module.operations.constants import AGGREGATE_FUNC
from src.operations_module.operations.base_operation import BaseOperation


class AggregateOperation(BaseOperation):

    def __init__(self, args):
        self.aggregate = args.aggregate


    def operation_on_table(self, table_data: list[dict]) -> list:
        column, method_aggregate = self.aggregate.split("=")
        values = map(lambda x: self.simple_validation(x[column]), table_data)

        if method_aggregate in AGGREGATE_FUNC:
            result = AGGREGATE_FUNC[method_aggregate](values)
            if method_aggregate == "avg":
                result /= len(table_data)

            table_data = [{method_aggregate: result}]

        return table_data