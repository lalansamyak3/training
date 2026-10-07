"""type hint tell that what type you expect from a variable to be"""

# type hint with variables
from typing import Optional, Union

age: int = 12
name: str = "samyal"
salary: float = 11223.33
print(age)
print(salary)


# just give the type suggestions like suggesting you the type
name1: str = 33
salary22: int = "samyak"
print(name1)
print(salary22)
print(salary)

namer: str = 12233
print(namer)


"""type suggestions in function"""


def print1(a: int, b: int) -> int:
    print(a + b)


print1(12, 13)


"""string type hints"""


def print2(name: str) -> str:
    print(f"hello my name is {name}")


print2("samyak")

namess = ["samyak", "age"]
namess = list[str]


"""type suggestion for list now"""
namess1: list[str] = ["sam", "efrrfrf"]
print(namess1)


phoneno: list[int] = [123344, 12444, 13322323]
print(phoneno)


"""functions with list"""


def printg(numberi: list[int]) -> int:
    return sum(numberi)


"""dict[str,int]"""

marks: dict[str, int] = {"maths": 12, "social": 24, "science": 26}


"""another example"""
details: dict[str, int] = {"maths": 23, "phoneno": 2433434, "age": 12}
print(details)


"""dictionary with list values"""

details122: dict[str, list[int]] = {"name": [1, 2, 3], "age": [12, 34, 55]}
print(details122)


"""dictionary with dictionary values"""

dict222: dict[str, dict[str, int]] = {"name": {"name": 12, "age": 21, "gender": 0}}


"""type hints in tuples too now"""

t1: tuple[str, int] = ("1", 12)
print(t1)

t2: tuple[int, ...] = (1, 2, 3, 4, 5)
print(t2)


"""sets type int now"""
set1: set[str] = {"samyak", "samyak", "heyy"}
print(set1)

set2: set[int] = {1, 2, 2, 3, 4, 4}
print(set2)


"""now optional here"""
age23: Optional[int] = None


"""why is optional useful it return either the none or something"""


def printi(age: int) -> Optional[str]:
    return f"my age is {age}"


"""union in typescripts"""
aggg: Union[int, str]
value: int | str = "samyak"

# union old and new syntax is given above
print(value)
print(aggg)


"""type alias now"""
marks1: dict[str, int]

student_marks: marks1 = {"samayak": 21, "ramanb": 23}
print(student_marks)


"""type hint with the nested structure now"""
details223: list[dict[str, int | list[int] | str]] = [
    {
        "name": "samyak",
        "age": 21,
        "gender": "male",
        "phoneno": [1212223, 2322323, 23233223],
    }
]
print(details223)
