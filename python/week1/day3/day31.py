x = [1, 2, 3, 4]
sq = []
for i in x:
    sq.append(i**2)


"""list compreghensions now"""

y = [i**2 for i in x]
print(y)

"""adding 10 to evbery number"""
z = [i + 10 for i in range(4)]
print(z)


"""convert the strings now"""

m = ["sam", "ran", "ten"]
o = [i.upper() for i in m]
print(o)


"""extract the len"""

p = [len(i) for i in m]
print(p)


"ist compreghension from range" ""
f = [i**3 for i in range(5) if i % 2 == 0]
print(f)


"""conditional compreghensions"""

# this is filtering if if is used after for loop
# #if at the end is filtering
# onluy for spmeitems means it will not work for all the items of iterables
po = [x * 2 for x in range(4) if i % 3 == 0]
print(po)
numberi = [23, 45, 66, 2]
ro = [x * 2 for x in numberi if x > 3]


# this is conditional compreghensions
# numberi=[23,45,66,2]
# if else at the starting is =conditional value
# work for all the itms of the ietrables
# no of outputs = no of nymbers in utearbels

gp = ["even " if x % 2 == 0 else "odd" for x in numberi]
print(gp)

"""another example of conditionbal comprehensions """
numbl = [12, 14, 16, 19, 22]
ji = [i**2 if i > 15 else i for i in numbl]
print(ji)


"""multiple conditions"""
pl = [x for x in range(19) if x > 2 and x % 2 == 0]
print(pl)
pi = [x for x in range(8) if x > 23 or x % 2 == 0]

"""strining filters"""
ri = ["ram", "shyam", "kisan"]

hi = [name for name in ri if name.startsWith("a")]
print(hi)


"""dictionary compreghensions"""
oi = {x: x * 2 for x in range(12)}
print(oi)

# { key : value   for item in iterable }
# down is the normal approach
"""numbers = [1, 2, 3, 4]

squares = {}

for number in numbers:
    squares[number] = number ** 2"""


"""dictionary comprehensions with name"""
kl = ["shanu", "sita", "sonu"]
jo = {name: len(name) for name in kl}
print(jo)


"""dict compre with range"""
lp = {i: i**2 for i in range(23)}
print(lp)


"""dict with filters"""
nj = {i: i**2 for i in range(12) if i % 2 == 0}
print(nj)

"""tranforming extisting dicyionary """
dict1 = {"mango": 13, "apple": 12, "chokoo": 134}
new_prices = {name: prices * 10 for name, prices in dict1.items()}
print(new_prices)


"""conditional dictionary values"""
opi = {x: "even" if (x % 2 == 0) else "odd" for x in range(20)}
print(opi)


"""set comprehensions """
# work sme as list comprehensions but dont allow duplicate s thats whuy it is used
set1 = {x**2 for x in range(20)}
print(set1)


"""set compreghension with filtering"""
f = {x**2 for x in range(20) if x % 2 == 0}
print(f)
# If you need if-else, the conditional expression goes before for:

"""comprehension with functions"""


def square(x):
    return x**2


numbert = [1, 2, 3, 4]
xt = [square(x) for x in numbert]
print(xt)


"""list comprehension for fastapi"""

json1 = [
    {"name": "samyak", "age": 21},
    {"name": "samo", "age": 23},
    {"name": "di", "age": 13},
]
list1 = [user["name"] for user in json1]
print(list1)

list22 = [user["name"] for user in json1 if user["age"] > 18]
print(list22)


"""dictionary comprehensions with fastapi"""

userss = [{"name": "sam", "age": 21}, {"name": "sheetal", "aghe": 22}]
xi = {user["name"]: user["age"] for user in userss}
print(xi)


"""dictionary comprehension with filtering"""
dict33 = [
    {"id": 1, "name": "sam", "age": 22},
    {"id": 2, "name": "saii", "age": 25},
    {"id": 3, "name": "iin", "age": 18},
    {"id": 4, "name": "spp", "age": 27},
    {"id": 5, "name": "nop", "age": 19},
]

ppp = {user["id"]: user["name"] for user in dict33 if user["age"] > 18}
print(ppp)


"""comprehension with enu,erate"""
names = ["Samyak", "Rahul", "Aman"]

result = [f"{index}: {name}" for index, name in enumerate(names)]

print(result)


"""comprehensiosn with zip"""
nama = ["sm", "di", "rii"]
age = [12, 14, 33]
poo = {name: age for name, age in zip(nama, age)}
print(poo)


"""list comprehension vs genratores"""

l12 = [x * 2 for x in range(29)]
print(l12)
l21 = (x * 2 for x in range(29))
print(l21)
# genrators produces value lazily only genrateds the value when needed


"""truthiness   in python"""
print(bool({}))
print(bool(range(0)))
print(bool(false))
print(bool(0))
print(bool(0.0))
print(bool(oj))
print(bool([]))
print(bool(()))
print(bool(None))
print(bool(""))
# empty string is also falsy


# these values are treated by defauilt as falsse only in python

loggin = False
if loggin:
    print("opening page")
else:
    print("no bening looged in")

# out[ut is else will exceute no bening logged in


# negative numbers are also true
print(bool(-1))
print(bool(-100))


# non zero or non empty value always true
print(bool(0j))
print(bool(1.0))


# non empty string is not falsy even whitespace is true

# true
print(bool(" "))
"""ne => False
0 => False
0.0 => False
0j => False
'' => False
[] => False
() => False
{} => False
set() => False
range(0, 0) => False"""

username = ""
if username:
    print("hii")
else:
    print("bye")
# output is bye as empty string is comnsidered as false on;ly

if not username:
    print("hii")
else:
    print("bye")
# output is hiii as empty string is false and (bnot false)=true so hii is output


"""truithiness with and """
# truw as both exust
name = "samy"
age = 12
if name and age:
    print("hello")
else:
    print("bye")

# output is bye


"""importnat concepts """
print("samyak" and 22)
# output is 22 because boyth value existy and acc to truthiness an i 22

print("" and 22)
# output is "" as """ is false


"""truthiness with or """
name = ""

print("" or 22)
# output is 22 now

"""real worlkd pattern"""
namer = input("enetr the name")
if not namer:
    print("plss enetr the name")
# if namer is "" then false not fals eis true so output is enetr the name if namer is not empty
# means true and not true is false so dont excecutes


print(bool("0"))
# output true string is not empyy
print(bool(""))
# output is false


data = [false]
print(bool(data))
# output is true as list is not empty

ap = [0]
print(bool(ap))
# output is true


it = {"age": 22}

if not age:
    print("hello")
# use is or in not (not) here
# is is also used for truthiness like using not age  we can use is not
###IMpirtantConcpet above


poi = [[]]
print(bool(pi))
# the above output is true as list is not epty haviing another list

"""truthiness with functions"""


def print():
    return ""


user = print()
if user:
    print("user found")
else:
    print("no user found")
# out[put is no user found as empty string is falsy


"""truthiness with api respionse"""
rep = {"user": []}
if rep["user"]:
    print("exist")
else:
    print("not eist")
# output s not exist as user is empty list as value and e,pty list vaulue is falsy


"""truthiness with default values"""
print("" or "samyak")
# oitput is samyak
print("hello" or "samyal")
# output is hello

# __bool__ and __len__ is used by pthon for truthiness
# __len__ is zero vvalue is falsy
