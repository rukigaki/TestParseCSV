# from src.operations_module.operations.aggregate_operation import AggregateOperation
# from src.operations_module.operations.filter_operation import FilterOperation
# from src.operations_module.operations.order_operation import OrderByOperation

from .operations import *



class Operations:
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