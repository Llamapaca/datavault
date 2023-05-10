from datavault import DataVaultModel, Attribute, BusinessKey


class Sat(DataVaultModel):
    name = Attribute(dtype=str)
    surname = Attribute(dtype=str)
    telephone = Attribute(dtype=int)
    hash_key = BusinessKey(["name", "surname", "telephone"])

    


class Lnk(DataVaultModel):
    hash_key = BusinessKey(["name", "surname", "telephone"])


def main():
    sat1 = Sat.from_dict({"name": "Guido", "surname": "Rossum", "telephone": 598433322})
    print(repr(sat1))

    sat2 = Sat.from_dict(
        {"name": "NotGuido", "surname": "Rossum", "telephone": 598433322}
    )
    print(repr(sat1))
    print(repr(sat2))

    return sat1


if __name__ == "__main__":
    sat = main()
