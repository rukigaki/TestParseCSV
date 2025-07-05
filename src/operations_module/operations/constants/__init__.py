"""
Пакет, который содержит Enum Классы.
Это внутренний пакет, который не выходит из области видимости пакета operations
"""


__all__ = (
    "AggregateEnum",
    "ComparisonEnum"
)

from .aggregate_func import AggregateEnum
from .operator_func import ComparisonEnum