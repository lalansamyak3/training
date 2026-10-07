"""Exception is an error which comes when program is running."""

sgr = int(input("Enter the number"))
# if sgr is a string it will cause ValueError

# program 1
try:
    age = int(input("Enter the number"))
except ValueError:
    print("Wrong entered")


# program 2
store = int(input("Enter the number"))
try:
    number = 10 / store
except ZeroDivisionError:
    print("Divided by zero")


# program 3 TypeError
value = 12
age = "nnk"

try:
    print(value + age)
except TypeError:
    print("Wrong type entered")


# program 4: NameError
try:
    print(username)
except NameError:
    print("Username does not exist")


# program 5: IndexError is there
l1 = [1, 2, 3, 4]

try:
    print(l1[9])
except IndexError:
    print("Out of index error")


# program 6: KeyError

dict1 = {"name": "samyak", "age": 21, "gender": 21}

try:
    dict1["email"]
except KeyError:
    print("Key does not exist")


# program 7
# AttributeError: object doesn't have the method
s = "samyak"

try:
    s.append("ehlni")
except AttributeError:
    print("Attribute doesn't exist")


# program 8: Multiple exceptions
try:
    h = int(input("Enter the number"))
    m = 10 / h
except ValueError:
    print("Wrong value entered")
except ArithmeticError:
    print("Zero division error occurred")


# as e
try:
    m = 10 / 0
except ArithmeticError as e:
    print(e)


"""try except else finally"""
"""finally always executes no matter if exception comes or not, always it executes"""

try:
    kl = int(input("Enter the number"))
except ValueError as e:
    print(f"The error is {e}")
else:
    print(kl)
finally:
    print("Hello")


"""Raise: sometimes you want to create an exception yourself"""

age = -4

if age < 0:
    raise ValueError("Can't be negative")


"""Real backend example
"""


def adduser(age):
    if age < 18:
        raise ValueError("User should be greater than 18")
    return "Added"


try:
    call = adduser(20)
    print(call)
except ValueError as e:
    print(f"ValueError occurred now: {e}")


# program 8: FileNotFoundError
try:
    file = open("sam.txt")
except FileNotFoundError:
    print("File doesn't exist")


"""PermissionError: occurs when a file doesn't permit us to make changes to it.
We cannot open it for writing."""


# program 8
# IsADirectoryError
try:
    open("my_folder", "w")
except IsADirectoryError:
    print("It isn't a file, it is a directory")


# ImportError program 9
try:
    from math import something
except ImportError:
    print("Something doesn't exist in the math package")


# program 10
try:
    import pandas a
except ModuleNotFoundError:
    print("No module exists")


# program 10
# OverflowError
# when number produced is too large
import math

try:
    math.pow(3, 100000)
except OverflowError:
    print("Overflow error is there")


# program 11
# RecursionError
try:

    def hello():
        hello()

    hello()

except RecursionError:
    print("Recursion error in the function")


# StopIterationError
number1 = iter([10, 20, 30])

print(next(number1))
print(next(number1))
print(next(number1))

try:
    print(next(number1))
except StopIteration:
    print("Stop iteration error")


"""KeyboardInterrupt exception: when user is running a program
and presses Ctrl + C, then KeyboardInterrupt occurs."""


#########################################################################################################

# Creating our own custom exceptions
# Custom exceptions are created based on the situations you want, like:
# UserNotFound, InvalidDataEntry


class invalidage(Exception):
    pass


def adduser(age):
    if age < 18:
        raise invalidage("Can't be negative")
    return "Added"


try:
    adduser(20)
except invalidage:
    print("Invalid age")


"""raise: you create or trigger an exception
except: you handle an exception"""


#################################################################################################

"""One real backend example now"""

"""Use of CUSTOM EXCEPTION IN BACKEND NOW"""

####### CUSTOM EXCEPTIONS ##############


class usernotfoun(Exception):
    pass


dict1 = [
    {"id": 1, "name": "samyak", "age": 22},
    {"id": 2, "name": "sak", "age": 23},
    {"id": 1, "name": "dd", "age": 22},
    {"id": 1, "name": "samyak", "age": 21},
]


def checkuser(id):
    for i in dict1:
        if i["id"] == id:
            return i

    raise usernotfoun("User not found")


try:
    ab = checkuser(2)
    print(ab)
except usernotfoun:
    print("User not found")


"""Custom exceptions: suppose you are having a banking application"""
"""Payment failed, UserNotFound"""
"""User not found, Invalid details, Account not found.
These are the exceptions in a banking application.
So normal exceptions will not work, so for that we need custom exceptions."""


"""IN PRODUCTION APPLICATION WE WILL NEED TO CREATE MULTIPLE CUSTOM EXCEPTIONS
by creating multiple exception classes"""


"""Don't catch every exception

Example:

def cal():
    return 10 / 0

try:
    cal()
except Exception:
    pass

print("Sut found, Invalid details, Account not found.
These are the exceptions in a banking application.
So normal exceptions will not work, so for that we need custom exceptions."""


this will give you an error

Here the exception is swallowed."""


# EXCEPTION HANDLING IN FASTAPI
"""
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/call/{student_id}")
def get_user(student_id: int):

    if student_id != 1:
        raise HTTPException(status_code=404, detail="No user found")

    return {"name": "samyak", "age": 21}
    
