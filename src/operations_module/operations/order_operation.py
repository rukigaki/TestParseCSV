from src.operations_module.operations.base_operation import BaseOperation


class OrderByOperation(BaseOperation):
    def __init__(self, args):
        self.order_by = args.order_by


    def operation_on_table(self, table_data: list[dict]):
        """
        см. -> base_operation.operation_on_table
        """

        column, value = self.order_by.split("=")

        def asc_or_desc():
            if value == "asc":
                return False
            elif value == "desc":
                return True
            raise ValueError("Неверное значение! Должно быть: asc или desc!")

        table_data = sorted(table_data, key=lambda x: self.simple_validation(x[column]), reverse=asc_or_desc())

        return table_data
