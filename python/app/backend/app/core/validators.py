import re
from datetime import date


def calculate_age(dob: date) -> int:
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def validate_password_strength(value: str) -> str:
    problems = []
    if len(value) < 8:
        problems.append("at least 8 characters")
    if len(value) > 64:
        problems.append("at most 64 characters")
    if not re.search(r"[A-Z]", value):
        problems.append("an uppercase letter")
    if not re.search(r"[a-z]", value):
        problems.append("a lowercase letter")
    if not re.search(r"\d", value):
        problems.append("a digit")
    if not re.search(r"[^A-Za-z0-9]", value):
        problems.append("a special character")
    if problems:
        raise ValueError("Password must contain " + ", ".join(problems))
    return value


"""calculate_age(dob)

python
return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
Starts with the year difference (today.year - dob.year).
Subtracts 1 if the birthday hasn’t happened yet this year. The tuple comparison (today.month, today.day) < (dob.month, dob.day) returns True (counts as 1) or False (counts as 0).
Example: born 2000-12-25, today 2026-10-13 gives 26 - 1 = 25.

validate_password_strength(value)

It collects every rule the password breaks, then reports them all at once:

Length between 8 and 64 characters.
At least one uppercase letter, lowercase letter, digit, and special character (anything not a letter or number, via [^A-Za-z0-9]).

If anything fails, it raises ValueError with a message like:
Password must contain at least 8 characters, an uppercase letter, a digit"""
