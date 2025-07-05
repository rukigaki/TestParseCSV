from enum import Enum


class AggregateEnum(Enum):
    MAX = ("max", max)
    MIN = ("min", min)
    AVG = ("avg", sum)