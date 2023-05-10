from typing import Any, Callable, Self
from .field import Attribute, BusinessKey


class DataVaultModel:
    __attrs: dict[str, Attribute]
    __keys: dict[str, BusinessKey]
    hash_func: Callable[[BusinessKey, dict[str, Any]], str]

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
        kwargs = {}
        for key, value in cls.__attrs.items():
            kwargs[key] = value.dtype(data[key])

        for key, value in cls.__keys.items():

            hash_attrs = [str(data[_val]) for _val in value.hash_attrs]
            hash_str = "||".join(hash_attrs)
            kwargs[key] = hash_str

        inst = cls()
        inst.__dict__.update(kwargs)
        return inst

    def __str__(self) -> str:
        return type(self).__name__ + str(
            {key: value for key, value in self.__dict__.items() if "__" not in key}
        )

    def __repr__(self) -> str:
        return type(self).__name__ + str(
            {key: value for key, value in self.__dict__.items() if "__" not in key}
        )
