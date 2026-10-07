name = "samyak"
print(name)
print(name[0])
print(name[-1])
print(name[1:4])
print(name[1:2:2])

"""satrings are immutable cannot be changes so we need to make new"""
# but can be reaiisned
name1 = name + "s"
print(name1)

name2 = name[0:3] + "l" + name[4:]
print(name2)

name = "sam"
print(name)

# reassisgnmentof values above
# deleting the whole string
del name

# name no longer exists after del, so recreate it for the examples below
name = "sam"

# reversing the string
print(name[::-1])
print("".join(reversed(name)))


# string are immutable original never changes so store it in list
name2 = "samyak"
l1 = list(name2)
l1[2] = "o"
print(l1)
print(" ".join(l1))


name3 = """helllo my name is """
print(name3)
print(name1.upper())
print(name1.lower())
print(name3.strip())
print(name3.replace("my", "hiii"))

rt = ["my", "name", "is"]
print(" ".join(rt))

print(name3.find("my"))
print(name3.count("m"))
print(name3.startswith("m"))
print(name3.endswith("heuyyy"))

name4 = input("enetr the name: ")
print(name4)
print(f"hello my name is {name4}")

age = int(input("enetr the age: "))
print(f"my name is {name4} and age is {age}")


"""list and its methods now"""

l1 = [1, 2, 3, 4, 5]

for i in l1:
    print(i)

for i in range(10):
    print(i)

for i in range(len(l1)):
    print(i, l1[i])

l1.append(10)
print(l1)

l1.insert(2, 123)
print(l1)

l1.remove(4)
print(l1)

l2 = [34, 45, 56]
l1.extend(l2)
print(l1)

l3 = ["samyak", 12, 445]

print(l1[0])
print(l1[2])
print(l1[-1])


"""slicing in list"""
print(l1[0:3])

"""list are mutable"""
print(l1)

l1[2] = 600
print(l1)

l1.pop()

l1.sort()
print(l1)

# reverse() changes the list and returns None
l1.reverse()
print(l1)

print(len(l1))


"""list memebership"""
print(10 in l1)
print(12 not in l1)


"""list comprehensions"""
sq = [i * i for i in range(10)]
print(sq)

check = [i * i for i in range(20) if i % 2 == 0]
print(check)


"""now tupples"""

t1 = (1, 2, 3, 4, 5)

print(t1)
print(t1[0])
print(t1[-1])
print(t1[0:3])


"""tupples are immutables"""
# t1[0] = 92892
# print(t1)

# The above gives TypeError because tuples are immutable.


"""tupples unpacking"""
m1, m2, m3, m4, m5 = t1

print(m1)
print(m2)
print(m3)
print(m4)
print(m4)


"""see the diffrence"""
z1 = 10
print(type(z1))

z2 = (10,)
print(type(z2))


"""tupples methods here"""
print(t1.count(12))
print(t1.index(3))

zz = [1, 2, 3, 4, 5, 5, 6, 6]

print(zz.index(6))
print(zz.index(6, 7))


"""tupples operations now"""
print(len(zz))
print(max(zz))
print(min(zz))
print(sum(zz))


"""membership operator in tupples"""
print(344 in t1)
print(344 in zz)


"""tuplles indexing now"""
print(t1[0])


"""tupples slicing"""
print(t1[0:3])


"""tupples concatenation now"""
b1 = (12, 23, 3)
b2 = (2, 4, 334)

b3 = b1 + b2
print(b3)


"""tuplles mrepeitition"""
xc = (12, 34, 4343)
print(3 * xc)


"""tupple unpacking"""
l1 = (1, 2, 3)

w1, w2, w3 = l1

print(w1)
print(w2)
print(w3)


"""tupple s extended unpacking now"""
lz = (1, 2, 3, 4, 5, 5)

r1, *r2, r3 = lz

print(r1)
print(r2)
print(r3)


"""tupple sare immutables"""
# lz[0] = 100
# print(lz)

# The above gives TypeError because tuples are immutable.


"""conertimg tupple to lis"""
t0 = (12, 34, 45)

list33 = list(t0)

print(t0)
print(list33)

list33.append(12)
print(list33)

t0 = tuple(list33)
print(t0)


"""dictionary from here"""

# it stores the data in the form of key value pair

dict1 = {"name": "samyak", "age": 12, "gender": "male"}

print(type(dict1))


"""dictionary iteration from here"""

for i, j in dict1.items():
    print(i, j)

for i in dict1.values():
    print(i)

for i in dict1.keys():
    print(i)


"""accesimg the avlues in dict"""
print(dict1["name"])


"""adding another key value pari in the dictionary"""
dict1["salary"] = 123444

print(dict1)


"""methods of dictionary now"""

"""used wehen ypu are not sure if key exist"""
print(dict1.get("name"))

print(list(dict1.keys()))
print(list(dict1.values()))
print(dict1.items())


"""updating a value in dictionary"""
dict1["name"] = "samyak lalan"

print(dict1)


"""remove a key in dict"""
dict1.pop("salary")
print(dict1)


"""membership in dictionary"""
print("name" in dict1)
print("gender2" in dict1)


"""nested dictionary"""
dict44 = {
    "name": "samyak",
    "age": 21,
    "gender": "male",
    "details": {"salary": 12223, "city": "indore"},
}

print(dict44["name"])
print(dict44["details"]["city"])


"""list of dictionary and ow to take out specific details from here"""
"""This is extremely important for backend/API/AI work."""

l23 = [
    {"name": "samyak", "age": 12, "gender": "male", "salary": 112232},
    {"name": "sa", "age": 123, "gender": "female", "salary": 112232},
]

print(l23[0]["gender"])


"""SETS"""

# set store on;y unique elements
ooo = {12, 3, 3, 3, 45, 55}
print(ooo)


# see the diffremncves now
print(type(ooo))

# sets is unordered and unindexed
# print(ooo[0]) will give eror


"""sets methods now"""
ooo.add(234)
print(ooo)

ooo.remove(12)

# discard is safer than remove if it doesnt exist or you are not sure about the exiustence
ooo.discard(45)

mmm = {12, 3, 4, 5}

"""union operation of set"""
print(mmm | ooo)

"""intersection of set"""
print(mmm & ooo)

"""difrence insets"""
print(mmm - ooo)
