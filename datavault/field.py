from dataclasses import dataclass
from decimal import Decimal
from typing import Type


DTYPE = Type[str | int | float | bool | Decimal]


@dataclass
class Attribute:
    dtype: DTYPE
    nullable: bool = False
    description: str = ""


@dataclass
class BusinessKey:
    hash_attrs: list[str]
