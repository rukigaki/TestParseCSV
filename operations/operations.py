from .constants import OPERATORS, AGGREGATE_FUNC


class Operations:
    __slots__ = ("where", "aggregate", "_methods")

    def __init__(self, arg) -> None:
        self.where = arg.where
        self.aggregate = arg.aggregate

        self._methods = {
            self.aggregate: self.__aggregate_operation,
            self.where: self.__filter_operation,
        }


    def __call__(self, table_data) -> list:
        table = table_data
        for method in self._methods:
            if method is None:
                continue

            table = self._methods[method](table)

        return table


    def __filter_operation(self, table_data) -> list:
        for operator_key in OPERATORS:
            if operator_key in self.where:
                column, value = self.where.split(operator_key)
                operator_func = OPERATORS[operator_key]

                table_data = [row for row in table_data
                              if operator_func(self.simple_validation(row[column]),
                                                self.simple_validation(value))]
                return table_data

        raise ValueError("Отсутствует оператор сравнения!")


    def __aggregate_operation(self, table_data) -> list:
        column, method_aggregate = self.aggregate.split("=")
        values = map(lambda x: self.simple_validation(x[column]), table_data)

        if method_aggregate in AGGREGATE_FUNC:
            result = AGGREGATE_FUNC[method_aggregate](values)
            if method_aggregate == "avg":
                result /= len(table_data)

            table_data = [{method_aggregate: result}]

        return table_data


    @staticmethod
    def simple_validation(value) -> int | float | str:
        for cast in (int, float):
            try:
                return cast(value)
            except ValueError:
                continue
        return value