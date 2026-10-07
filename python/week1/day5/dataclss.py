"""dataclases is one of the inportant features"""

"""dtaclases used to automaticaaly genrate metods such as __init__() and __repr__()
from annotated firelds
"""
"""dataclasses is the conveint way to store the data you dont ned __init__,__eq__,__repr__"""

from dataclasses import dataclass, field


@dataclass
class Abc:
    name: str
    age: int
    gender: str
    marks: list[int]


s = Abc("samyak", 21, "male", [10, 20, 30, 30])
print(s)  # this is for __repr__
s1 = Abc("samyak", 21, "male", [10, 20, 30])
print(s == s1)  # __eq__

# out[ut=Abc(name="samyak",age:21,marks:[10,20,30])
"""here you can see you dont have used __init__ and __repr__  dataclasses genrated it for you"""


"""dataclases with methods"""


@dataclass
class di:
    name: str
    age: int
    gender: str
    marks: list[int]

    def cal(self) -> float:
        return sum(self.marks) / len(self.marks)


dd = di("samyalk", 21, "male", [10, 20, 30])
print(dd)
print(dd.cal())


"""Default values in dataclass"""


@dataclass
class ki:
    name: str
    age: int
    gender: str
    city: str = "indore"


ee = ki("samyak", 21, "male", "ratlam")
ff = ki("raj", 22, "male")
print(ee)
print(ff)


""""""
################################################################################################
"""Field()"""
"""it helps you toi customize the fielsds used for more advances dataclass configurattyoons """


# Program1 for deafult factory
class mh:
    name: str
    age: int
    marks: list[int] = field(default_factory=list)
    # default factyory =list means will give a new list for ever object


s1 = mh("samyak")
print(s1.marks)  # will give ypu []
# default_factory =true mtlbe ist for every object
s1.marks.append(10)
print(s1.marks)

s2 = mh("amay", 21, [10, 20])
print(s2.marks)
print(s2.marks.append(30))
print(s2.marks)

# always for mutable like list and dictionary use default_factory=true


# progarm 2 for default factory
class ll:
    name: str
    age: int
    details: dict[str, str] = field(default_factory=dict)


s1 = ll("samyak")
print(s1.details)
s1.details["city"] = "indore"
print(s1.details)
s1.details["gender"] = "male"
print(s1.details)
# program3 for deafult values
"""fiels with deafult"""


class m:
    name: str
    age: int = field(default=11)


rr = m("samyak")
print(rr)
rt = m("samyak", 22)
print(rt)


# program 4 for we can have functions too in default_factory
def create(self):
    return ["puython", "java"]


@dataclass
class kl1:
    name: str
    age: int
    subjects: list[str] = field(default_factory=create)


# every new object call the create function

krt = kl1("samyak", 21)
print(krt)


"""'set """


# program 5 for the set
@dataclass
class Student:
    name: str
    skills: set[str] = field(default_factory=set)


s1 = Student("Samyak")

s1.skills.add("Python")
s1.skills.add("FastAPI")

print(s1)

# profrma6
"""init=false featur of field """
# field(init=false) meamns the firled will not come in the comstructor now
# so you cannot initialize it using the constructiror now


class jk:
    name: str
    age: int
    marks: list[str] = field(init=False)


mm = jk("samyak", 21)
print(mm)
# jl=jk("nkmn",21,[10,20,30])
# we wi;; cause an eror now


# prorram 7
"""repr=false"""


class jkg:
    name: str
    age: int
    marks: list[str] = field(repr=False)


mm = jk("samyak", 21, [10, 20, 30])
print(
    mm
)  # it will not show marjks in the represntation all other items will be shown not the marks


# program 6 compare=false
"""normally in comparing the obj it compare  every firls but using the compare =false 
will complete all other field but not that filed on which it is applied 
"""


class jm:
    name: str
    age: int
    marks: list[str] = field(compare=False)


mm = jk("samyak", 21, [10, 20, 30])
print(mm)
gg = jk("samyak", 21, [23, 22, 34])
print(gg)
print(mm=gg)  # it will give true as it is comparing two firlds not the marks field

# program 7 kw_only=true
"""constructor must be with the keyword argument not the postional 
like if we apply kw_ionly on name then calling it ab=krj(name"samyak ,21,"male")"""


class krj:
    name: str = field(kw_only=True)
    age: int
    marks: list[str]


# mm=krj("sam",21,[10,20,30]) will give an eror now
# rr=krj(name="samyak",21,[10,202,309]) this will also an eror as we cannot p[ass
# postional argument after keyword argument] will cayse an eor
po = krj(name="samyak", age=22, marks=[10, 20, 34])

print(po)


#####################################################################################################3
"""FROZEN"""
"""frozen dont allow uyou to make changes once obj is assisned a value you cannot update its value"""


@dataclass(frozen=True)
class dmm:
    name: str
    age: int


s1 = dmm("samyak", 21)  # __inity__
print(s1)  # repr__
# s1.age=23 #it will give an eror usig frozen we cannot reassisgned a aobhect onecuit is assisgned
# frozen still works with default factory s1.subjects.append still work
# program 2 fro frozen
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Student:
    name: str
    subjects: list[str] = field(default_factory=list)


s = Student("Samyak")

# s.name = "Rahul"
# will not work
# s.subjects = ["Java"]

# ✅ will work
s.subjects.append("Python")

# frozen also prevent from any kind of del of field
# like del s,.age

# frozen with inheritances


###########################################################################################################33

"""Order"""
"""order s used to genrate the compraiosn methods  like <,>,<=,>=,!="""


@dataclass(order=True)
class den:
    marks: int


ab = den(10)
cd = den(20)
print(ab=cd)


class fb:
    name: str
    marks: int


vv = fb("samyak", 22)
df = fb("may", 27)

print(vv > df)


"""with multiople field it act as tupple coparisons"""


@dataclass(order=True)
class l4:
    name: str
    age: int


m = l4("samyak", 21)
n = l4("rahul", 234)
print(m > n)
# this will give true as it compare them as tupples like (samyak,21)>(rahul,234)
# samyak is greater than rahul so true


@dataclass(order=True)
class l6:
    name: str
    age: int


m = l6("samyak", 21)
n = l6("samyak", 234)
print(m > n)
# ifirsly compare the first field if there are same then compare the next field 21>234 hence false


@dataclass(order=True)
class l4:
    name: str
    age: int


m = l4("samyak", 21)
n = l4("rahul", 234)
print(m > n)
# this will give true as it compare them as tupples like (samyak,21)>(rahul,234)
# samyak is greater than rahul so true


@dataclass(order=True)
class l8:
    name: str
    age: int = field(compare=False)


m = l8("samyak", 21)
n = l8("rahul", 234)
print(m > n)
# in this case it will give only compare the first fie;ld as the second field is already become
# fasle for the comparison


# Oder is used in sorting too
@dataclass(order=True)
class l4:

    age: int
    name: str


student = [l4(21, "samyak"), l4(33, "sinnn"), l4(34, "ednkn")]
student.sort()
# this will give true as it compare them as tupples like (samyak,21)>(rahul,234)
# samyak is greater than rahul so true


#########################################################################################################
"""POst__init__()"""
"""postinit :it is used to add more functionality to constructor
 as we know contrsuctor automatically is created in dataclass
so this is only used for self.name=name but we alsio want so,me more processing in it either 
we can use post__init__() it also works automatiocally as soon as 
the constructor comnplete dits excecution or we can create our own constructor instead of using a automatic one
"""

"""we can also use the normal methods but in case of normal methods we need to call it using th objects 
"""


@dataclass
class hnm:
    name: str
    age: int
    marks: int

    def __post_init__(self):
        if self.makrs < 0:
            raise ValueError("cant be negative")


dd = hnm("samyak", 21, 12)
d1 = hnm("raj", 22, -22)  # eror will be raised

"""either create the init from starting by yourseldf or use post_init__"""


############################POSTINIT WITH INITVAR####################################################
"""initvar : it is used only fpr creatimng the objects but not as the attributes for the objects
"""
from dataclasses import InitVar


@dataclass
class User:
    name: str
    password: InitVar[str]

    def __post_init__(self, password):
        print(password)


m = User("samyak", "abc123")
# opost__init__may give younpassword but if you try to do m.password will give eror
# only for creatiung the onbjects not used for the attributes of the objetcs

# program3 for postInit
"""post init with frozen equals to true """
"""POstInit with frozen=true"""


@dataclass(frozen=True)
class idk:
    name: str
    age: int
    result: str = field(init=False)

    def __post_init__(self):
        #     self.result = "Pass"
        # this will give an eror as frozen is true so changes cannot be made
        # nneedd to use object.__setattr__() if we want to still allow the changes
        if self.marks > 40:
            object.__setattr__(self, "result", "pass")
