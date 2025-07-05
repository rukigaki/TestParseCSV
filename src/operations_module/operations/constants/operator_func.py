from enum import Enum
import operator


class ComparisonEnum(Enum):
    EQ = ("==", operator.eq)
    GE = (">=", operator.ge)
    LE = ("<=", operator.le)
    GT = (">", operator.gt)
    LT = ("<", operator.lt)
    ASSIGN = ("=", operator.eq)