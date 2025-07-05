from src.operations_module.operations.base_operation import BaseOperation


class OrderByOperation(BaseOperation):
    def __init__(self, args):
        self.order_by = args.order_by


    def operation_on_table(self, table_data: list[dict]):

        column, value = self.order_by.split("=")
        order_by = True if value == "desc" else False
        table_data = sorted(table_data, key=lambda x: self.simple_validation(x[column]), reverse=order_by)

        return table_data
