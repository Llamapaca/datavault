from typing import Any, Callable, Self
from .field import Attribute, BusinessKey


class DataVaultModel:
    __attrs: dict[str, Attribute]
    __keys: dict[str, BusinessKey]

    def __init_subclass__(cls) -> None:
        cls.__attrs = {
            key: value
            for key, value in cls.__dict__.items()
            if isinstance(value, Attribute)
        }
        cls.__keys = {
            key: value
            for key, value in cls.__dict__.items()
            if isinstance(value, BusinessKey)
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        inst = cls()

        for key, value in cls.__attrs.items():
            inst.__dict__[key] = value.dtype(data[key])

        for key, value in cls.__keys.items():
            inst.__dict__[key] = value.hash_func(value.hash_attrs, data)

        return inst

    def __str__(self) -> str:
        return type(self).__name__ + str(
            {key: value for key, value in self.__dict__.items() if "__" not in key}
        )

    def __repr__(self) -> str:
        return type(self).__name__ + str(
            {key: value for key, value in self.__dict__.items() if "__" not in key}
        )
