# if statements
store = int(input("enetr the number"))
if store > 12000:
    print("hello")
else:
    print("bye")

if store > 20000:
    print("greater than 20000")
elif store == 20000:
    print("amount equal")
else:
    print("amt is less")

# if stos if excecutes at first
age = int(input("eneter the number"))
if age == 12:
    print("age is 12")
elif age >= 12:
    print("age is greater or equal to 12")
elif age < 12:
    print("sorry its less than 12")
else:
    print("hello dear")


# multiple if statements now
if age > 12:
    print("hello")
if age < 12:
    print("bye")


# nested if conditions
username = input("enetr the userbname")
password = int(input("enetr the password"))
if username == "samyak":
    print("now enetr the password")
    if password == 123:
        print("you are logged in now")

# nested if else
a = int(input("enetr the number"))
b = int(input("enet the number 2"))
c = int(input("enetr the number 3"))
if a > b:
    if a > c:
        print("a is greater  ")
    else:
        print("a is not gretaer than c  c is the gretaest ")
elif b > c:
    print("b is greater ")

    # comparison operators
    a = int(input("enetr the number"))
    b = int(input("enetr the number "))
    print(a == b)
    print(a > b)
    print(a < c)
    print(a >= b)
    print(a <= c)
    # comparing the strings now
    print("samyak" == "Samyak")
    print("samyak" == "denmarkl")
    print(a == b and b == c)
    print(a > b and b < c)

    # loops in python
    """LOOPS"""
"""for loops now"""
for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

l1 = [10, 20, 30]
print(l1)
print(l1[:3])
for i in l1:
    print(i)

for i in range(len(l1)):
    print(i)

t1 = (10, 20, 30, 40, 50)
for i in range(len(t1)):
    print(i)
dict1 = {"name": "samyak", "age": 12}
for i.j in dict1.items():
    print(i, j)

for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)

name = "samyak"
for i in range(len(name)):
    print(i)
for i in name:
    print(i)


# summation and factorial using loop
numeri = int(input("enetr the number"))
sum = 0
for i in range(0, numeri + 1):
    sum = sum + i
print(sum)


"""while loop"""
ab = 0
while ab < 123:
    print(ab)
    ab = ab + 1

print(range(10))
print(range(0, 10))
print(range(0, 10, 3))
for i in range(10, -1, -1):
    print(i)
print(list(range(10)))

for i in range(0, 10):
    print(i)
    if i == 4:
        break

for i in range(10):
    if i == 6:
        continue
    else:
        print(i)

iny = 0
while i < 5:
    print(i)
    i = i + 1

print(i)

for i in range(0, 10):
    print(i)

print(i)


"""real use case of break"""

am = ["ram", "shyam", "siya"]
for i in am:
    if i == "shyam":
        print("we got it")
        break


"""pass statement"""
for i in range(10):
    pass
# used as python dont allow empty blocks


"""nested for loops """
for i in range(0, 10):

    for j in range(0, i + 1):

        print("*", end=" ")
    print()

"""for-else loop now"""
for i in range(5):
    print(i)
else:
    print("hello")

"""for -else with break"""
# it will only print contaent of else if loop fully excecutes if not else content will not be printed then
for i in range(6):
    print(i)
    if i == 3:
        break
else:
    print("jello")
    # else will nort exceute in above scenario

    """while -else loop"""
mi = 0
while mi <= 3:
    print(mi)
    mi = mi + 1
else:
    print("cpmpleted the excecution now")
    # output =0,1,2,3,completed the exceution now

"""while-else with break"""
ci = 0
while ci <= 4:
    print(ci)
    ci = ci + 1
    if ci == 3:
        break
else:
    print("completed")
    # here output will be 0,1,2,3 only as the loop not completed its excecution

    """for else with continue"""
    vi = 0
    for i in range(5):
        if i == 3:
            continue
        print(i)
    else:
        print("completed excecution")

    # it will work differently output=0,1,2,4 themn completed exceution

    """login attempts 3 times uisng for -el;se"""

    for i in range(3):
        password = input("enter the paswword")
        if password == "sam123":
            print("login sucess")
            break
    else:
        print("attempted 3 times now wait for 30 seconds")
