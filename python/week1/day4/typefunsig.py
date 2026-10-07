from typing import Optional


def add(x: int, y: int) -> int:
    return x + y


print(add(12, 23))

"""typehints only to get what need to be enetered and return type it will work ecen you font follow type suggestion only use dfor suggestion 
not for validaton"""


"""type hint for strings ,list,float"""


def bdd(m: list[str]) -> int:
    return sum(m) / len(m)


def cdd(name: str):
    print(f"hello muy name is {name}")


cdd("samyak")


def ddd(name: list[str]):
    for na in name:
        print(na)


def edd(dict1: dict[str, int]):
    print(dict1["name"])


def imfo() -> tuple[str, int]:
    print("samyak", 21)


"""optional values"""


def fdd(name: Optional[str] = None) -> str:
    print(f"hello my name is {name}")


def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello Guest"

    return f"Hello {name}"


def sub(x, y):
    return x - y


print(sub(23, 24))
