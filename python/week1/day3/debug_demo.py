def calculate_total(price, quantity):
    total = price * quantity
    discount = total * 0.10
    final_price = total - discount

    return final_price


"""
F5 to start theb debugger and run it till the breakpoint is reached"""
# f5 means continue
"""select the breakpoint click left on line and option will come to add breakpount"""
"""f10 means run one line at time then stop used for step flow"""  # stepin
"""f11 to go inside the function and f11 +shift to comeout"""  # stepout of function

price = 100
quantity = 5

result = calculate_total(price, quantity)

print("Final price:", result)


def multiply(a, b):
    result = a * b
    return result


def calculate():
    x = 10
    y = 20

    answer = multiply(x, y)

    print(answer)


calculate()


tax_rate = 0.18


def calculate(price):
    total = price * 2
    tax = total * tax_rate

    return total + tax


x = 100

"""debugging to see what value does x holds while prnting inoe the funcytion"""
"""used f5 tehn f10 and f11 to entervthe function and f11 agsin"""


def test():
    x = 20

    print(x)


test()


"""debbugginga loop"""
numbers = [10, 20, 30, 40]

for number in numbers:
    result = number * 2
    print(result)
    # just clcik f5 then exxcecute line by line using f10 help to underatsnd the flow also'''
    age = 17

if age >= 18:
    result = "Adult"
else:
    result = "Minor"

    """debugginga n api"""
    from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = {1: "Samyak", 2: "Rahul"}

    user = users.get(user_id)

    return {"user_id": user_id, "name": user}
