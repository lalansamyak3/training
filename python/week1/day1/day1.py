"""variables  in python"""

a = 12
print(a)
name = "samyak"
print(name)

salary = 1233444.44
print(salary)
print(type(a))
print(type(name))
print(type(salary))
list1 = [1, 2, 3, 4, 5, 67]
print(list1)
set1 = {1, 2, 33, 34}
print(set1)
print(type(set1))
print(tuype(list1))

typples1 = (1, 23, 44, 4)
print(type(typples1))
print(typples1)
# swapping in variables
m = int(input("enter the m"))
n = int(input("eneter the value of n"))
m, n = n, m
print(m)
print(n)
# multiple assisgning in variables
o, p = 12, 13
print(o)
print(n)
print(id(a))
print(id(p))
del a
print(a)
print(a == b)
list3 = [1, 2, 3, 4, 5]
list4 = list3
print(id(list3))
print(id(list4))
list3.append(9)
print(list3)
print(list4)
ji = [1, 2, 3]
ki = [1, 2, 3]
print(ji)
print(ki)
print(ji == ki)
print(ji is ki)


ab = 12
cd = ab
print(ab)
print(cd)
ab = 14
print(ab)
print(cd)

"""user input and arithmatic operators in python """
a = int(input("eneter the no"))
b = int(input("eneter the no"))
c = a + b
d = a - b
e = a / b
f = a * b
g = a // b
h = a % b
i = a**b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
"""assisgnment operators in puython"""
count = 100
print(count)
count = count + 1
print(count)
count = count * 3

print(count)
count = count - 2
print(count)
count = count / 2
print(count)
count = count**5
print(count)
count = count // 2
print(count)
count = count % 3
print(count)
count = count >> 2
print(count)
count = count & 1
print(count)
"""comparison operatore """
hi = int(input("eneter the no"))
gi = int(input("enetr the no"))
print(hi == gi)
print(hi != gi)
print(hi > gi)
print(hi < gi)
print(hi <= gi)
print(hi >= gi)

x = "samyak"
y = "jain"
print(x == y)

z = "samyak"

print(x == y and y == z)
print(x == y or x == z)

"""12. Logical Operators"""
zi = int(input("enetr the no"))
oi = int(input("enter the no"))
print(zi > 12 and oi > 12)
print(zi >= 14 or oi > 23)
oop = FALSE
print(not oop)

"""IDebtity operators"""
msd = 12
abc = msd
print(id(msd))
print(id(abc))
print(msd is abc)
print(a == b)

pl = [1, 2, 3, 4]
lp = [1, 2, 3, 4]
print(pl == lp)
print(pl is lp)
print(pl is not lp)


"""memebership operators in python """
namer = input("enetr the name ")
print("s" in namer)
li2 = [13, 3, 44, 5, 55]
print(5 in li2)
dict4 = {"name": "samyak", "Age": 13, "gendet": "male"}
print("name" in dict4)
print("Age" in dict4)
print("salary" not in dicty4)

set3 = {2, 4, 34}
print(4 in set4)

print(455 not in set3)


"""bitwise operators """

print(5 & 100)

po = int(input("enetr the no"))
go = int(input("eneter the jo"))
print(po & go)
print(po | go)
print(~po)
print(po ^ go)
print(po << 1)
print(go >> 1)


"""conditional opeartor (ternary)"""
ki = int(input("enetr the ki"))
f = "pass" if ki > 90 else "fail"

"""operator with differnet datatypes"""
print(12 + 13)
print("hello " + " " + "sam")
print("hello" * 3)
print(int("4") + 4)
"""datatypes in python"""
wa = 12
wb = "samyak"
wc = 123.444
wd = [12, 23, 44]
we = {1, 2, 3, 4}
wf = (2132, 2332)
wg = {"name": "dio", "gender": "male"}
wh = FALSE
