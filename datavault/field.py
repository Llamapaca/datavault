from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Callable, Type


DTYPE = Type[str | int | float | bool | Decimal]


@dataclass
class Attribute:
    dtype: DTYPE
    nullable: bool = False
    description: str = ""


@dataclass
class BusinessKey:
    hash_attrs: list[str]
    hash_func: Callable[[list[str], dict[str, Any]], str]
