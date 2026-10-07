"""
FUNCTIONS

A function is a block of code designed to perform a specific task.
Functions help with:

1. Reusability
2. Easy debugging
3. Easy testing
4. Better organization
5. Code maintainability
"""

# --------------------------------------------------
# 1. BASIC FUNCTION
# --------------------------------------------------


def add(x, y):
    return x + y


print(add(10, 20))


# --------------------------------------------------
# 2. FUNCTION WITH TYPE HINTS
# --------------------------------------------------


def addi(x: int, y: int):
    return x + y


print(addi(10, 12))


# --------------------------------------------------
# 3. FUNCTION WITH PARAMETERS
# --------------------------------------------------


def printi(x, y):
    print(f"my name is {x} and age is {y}")


printi("samyak", 12)
printi("som", 34)


# --------------------------------------------------
# 4. FUNCTION WITH MULTIPLE PARAMETERS
# DEFAULT ARGUMENTS
# --------------------------------------------------


def ad(a=0, b=0, c=0):
    return a + b + c


print(ad(12, 13, 14))
print(ad(10, 12))
print(ad(12))


# --------------------------------------------------
# 5. FUNCTION RETURNING A VALUE
# --------------------------------------------------


def asi(x, y):
    return x - y


am = asi(10, 2)
print(am)

al = asi(23, 4)
print(al)


# --------------------------------------------------
# 6. PRINT VS RETURN
# --------------------------------------------------


def gi(x, y):
    print(f"hello {x + y}")


gi(10, 20)

om = gi(10, 20)
print(om)

# Output will be:
# hello 30
# None
#
# Why?
# Because gi() is printing the result but not returning anything.
# When a function does not return anything, Python returns None.


def hi(x, y):
    return x + y


ab = hi(10, 20)
print(ab)


# --------------------------------------------------
# 7. RETURNING MULTIPLE VALUES
# --------------------------------------------------

"""
A function can return multiple values.

Python internally returns them as a tuple.
"""


def gi(x, y):
    total = x + y
    diff = x - y

    return total, diff


ab = gi(30, 30)

print(ab)


# Tuple unpacking

ni, mi = gi(20, 20)

print(mi)
print(ni)


# Unpacking the tuple

adi, subi = ab

print(adi)
print(subi)


# --------------------------------------------------
# 8. DEFAULT ARGUMENTS
# --------------------------------------------------


def printy(name="none"):
    print(f"hello my name is {name}")


printy("sam")
printy("baby")
printy()


# --------------------------------------------------
# 9. KEYWORD ARGUMENTS
# --------------------------------------------------

"""
Keyword arguments make function calls more readable.

Instead of depending on position:

imfo("samyak", "male", 21)

we can write:

imfo(name="samyak", gender="male", age=21)
"""


def imfo(name, gender, age):
    print(name, gender, age)


# Keyword arguments

imfo(name="samyak", gender="male", age=21)


# --------------------------------------------------
# 10. POSITIONAL ARGUMENTS
# --------------------------------------------------

imfo("samyak", "male", 21)


# This is INVALID:
# imfo(name="samyak", "male", 21)
#
# You cannot put positional arguments after keyword arguments.


# --------------------------------------------------
# 11. *ARGS
# --------------------------------------------------

"""
*args is used when we don't know how many
positional arguments we will receive.

*args collects the arguments into a tuple.

Example:

summ(10, 20)

Inside the function:

args = (10, 20)
"""


def summ(*args):
    return sum(args)


print(summ(10, 20))
print(summ(10, 20, 30))
print(summ(10, 20, 30, 40))


# --------------------------------------------------
# 12. SEEING WHAT *ARGS CONTAINS
# --------------------------------------------------


def printii(*args):
    print(args)


printii(10, 20, 30)
printii(10, 20, 30, 40)


# --------------------------------------------------
# 13. PRACTICAL USE OF *ARGS
# --------------------------------------------------

"""
We can use *args when we don't know how many
values the function will receive.

Example:
Calculating the average of any number of values.
"""


def printp(*args):
    return sum(args) / len(args)


print(printp(10, 20, 30))
print(printp(23, 33, 445))


# --------------------------------------------------
# 14. **KWARGS
# --------------------------------------------------

"""
**kwargs is used when we don't know how many
keyword arguments we will receive.

**kwargs collects keyword arguments into a dictionary.
"""


def gt(**kwargs):
    print(kwargs)


gt(name="samyak", age=21, gender="male")
gt(name="samyak", age=21)


# --------------------------------------------------
# 15. *ARGS VS **KWARGS
# --------------------------------------------------

"""
*args
    -> extra positional arguments
    -> stored as a tuple

**kwargs
    -> extra keyword arguments
    -> stored as a dictionary
"""


def ry(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


ry(12, 13, name="samyak", age=21, gender="male")


# --------------------------------------------------
# 16. *args CAN HAVE ANY NAME
# --------------------------------------------------

"""
The name 'args' is just a convention.

We can technically use any name after *.
"""


def gv(*name):
    print(name)


gv("hello", "ho")


# --------------------------------------------------
# 17. **kwargs CAN HAVE ANY NAME
# --------------------------------------------------

"""
The name 'kwargs' is also just a convention.

We can technically use any name after **.
"""


def gj(**names):
    print(names)


gj(name="sam", age=21, gender="male")


# --------------------------------------------------
# 18. COMBINING PARAMETERS
# --------------------------------------------------

"""
We can combine:

normal parameter
*args
keyword-only parameter
**kwargs
"""


def op(name, *args, age=21, **kwargs):
    print("name:", name)
    print("args:", args)
    print("age:", age)
    print("kwargs:", kwargs)


op("samyak", 12, 14, 5, age=22, nickname="sam", gender="male")


# --------------------------------------------------
# 19. UNDERSTANDING THE ABOVE FUNCTION
# --------------------------------------------------

"""
When we call:

op(
    "samyak",
    12,
    14,
    5,
    age=22,
    nickname="sam",
    gender="male"
)

Python stores the values like this:

name
    -> "samyak"

args
    -> (12, 14, 5)

age
    -> 22

kwargs
    -> {
        "nickname": "sam",
        "gender": "male"
       }
"""


# --------------------------------------------------
# 20. IMPORTANT SUMMARY
# --------------------------------------------------

"""
NORMAL PARAMETER

def add(x, y):
    ...


DEFAULT PARAMETER

def add(x=0, y=0):
    ...


POSITIONAL ARGUMENT

add(10, 20)


KEYWORD ARGUMENT

add(x=10, y=20)


*ARGS

def test(*args):
    ...

Extra positional arguments
are stored in a tuple.


**KWARGS

def test(**kwargs):
    ...

Extra keyword arguments
are stored in a dictionary.


RETURN

return sends a value back
to the place where the function was called.


PRINT

print() only displays something
on the screen.
"""


# --------------------------------------------------
# 21. SIMPLE FINAL EXAMPLE
# --------------------------------------------------


def student_info(name, *subjects, age=18, **details):

    print("Name:", name)
    print("Subjects:", subjects)
    print("Age:", age)
    print("Other details:", details)


student_info(
    "Samyak", "Python", "Java", "AI", age=22, city="Indore", college="Medi-Caps"
)
