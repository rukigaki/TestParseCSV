import operator # Модуль из стандартной библиотеки Python


OPERATORS = {
        "==": operator.eq,
        ">=": operator.ge,
        "<=": operator.le,
        ">": operator.gt,
        "<": operator.lt,
        "=": operator.eq
    }


AGGREGATE_FUNC = {
            "max": max,
            "min": min,
            "avg": sum
        }