from typing import Any
from datavault import DataVaultModel, Attribute, BusinessKey
from hashlib import md5


def hash_func(hash_attrs: list[str], data: dict[str, Any]) -> str:
    hash_attrs = [str(data[_val]) for _val in hash_attrs]
    hash_str = "||".join(hash_attrs)
    return md5(hash_str.encode("utf-8")).hexdigest()


class Sat(DataVaultModel):
    name = Attribute(dtype=str)
    surname = Attribute(dtype=str)
    telephone = Attribute(dtype=int)
    hash_key = BusinessKey(["name", "surname", "telephone"], hash_func=hash_func)


class Lnk(DataVaultModel):
    hash_key = BusinessKey(["name", "surname", "telephone"], hash_func=hash_func)

    hash_func = hash_func


def main():
    sat1 = Sat.from_dict({"name": "Guido", "surname": "Rossum", "telephone": 598433322})
    print(sat1)

    sat2 = Sat.from_dict(
        {"name": "NotGuido", "surname": "Rossum", "telephone": 598433322}
    )
    print(sat1)
    print(sat2)

    lnk = Lnk.from_dict(
        {"name": "NotGuido", "surname": "Rossum", "telephone": 598433322}
    )
    print(lnk)


if __name__ == "__main__":
    main()
