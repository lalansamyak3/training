class Student:
    def imfo(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_marks(self):
        return sum(self.marks) / len(self.marks)

    def print(self):
        print(self.age)
        print(self.name)
        print(self.marks)


s = Student()
s.imfo("samyak", 21, [12, 13, 45])
print(s.calculate_marks())
s.print()


"""PROGRAM 2"""


class stu:
    def cal(self, name="none", age=0):
        print(name)
        print(age)


sb = stu()
sb.cal()

"""PROGRAM3"""
"""constructor and super keyword now """


class Base:
    def __init__(self):
        print("its base class constructor ")

    def inpu(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def prt(self):
        print(self.name)
        print(self.age)
        print(self.salary)


"""PROGRAM 4"""


class child(Base):
    def __init__(self):
        super().__init__()
        print("its child class constructor now")

    def add(self, name, age, salary, gender, city):
        super().inpu(name, age, salary)
        self.gender = gender
        self.city = city

    def prt(self):
        super().prt()
        print(self.gender)
        print(self.salary)


c = child()
c.add("sam", 21, 122233, "male", "indore")
c.prt()


"""constructors"""
"""
class bb:
    def __init__(self):
        print("default constructor")
    def __init__(self, name,age):
        print(name)
        print(age)
    def __init__(self, name, bases, dict, /, **kwds):
        pass"""
"""constructor overloading is not su[proted in python only ovberriding is supported """

"""constructor overridding is here now """


class fd:
    def __init__(self, name, age, city):
        print("base class")
        print(name)
        print(age)
        print(city)


class fg(fd):
    def __init__(self, name, age, city, gender):
        super().__init__(name, age, city)
        print(gender)


as2 = fg("samyak", 21, "indore", "male")


"""seldf is the object of current class o only """


class n:
    def printo(self):
        print(self)


ann = n()
print(ann)
# yopu can see the printo() ,ethod and ann is same id

"""Instance variables """


class xx:
    def yuv(self, name, age):
        self.name = name
        self.age = age

    def gt(self):
        print(self.name)
        print(self.age)


ss = xx()
print(ss.name)
print(ss.gt())
ss.yuv("samyak", 21)
print(ss.gt())
print(ss.age)

"""INstance varibale sare self.name and self.age above """


"""Instance methods now """


class fc:
    def set(self, name, age, marks):
        print(name)
        print(age)
        print(marks)

    def cal(self):
        return sum(self.marks) / len(self.marks)


"""this is intance method you can see above easily"""
dm = fc("samyak", 21, [12, 33, 44])


"""Instanvce methods eith parameters """


class hj:
    def rnt(self, name):
        self.name = name

    def ll(self, mess):
        print(f"my name is {self.name} and {mess}")


hl = hj()
hl.rnt("sam")
hl.ll("hiii gm")


"""class varibles"""


class school:
    schoolname = "sriram"

    def add(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def imfo(self):
        print(self.name)
        print(self.age)
        print(self.schoolname)
        print(self.gender)


student1 = school()
student1.add("samyak", 21, "male")
student1.imfo()
student2 = school()
student2.add("ram", 222, "male")
student2.imfo()


"""CLASS METHOD S ARE USEDTO CHANGE THE CLASS VARIABLES """


class Dep:
    schoolname = "choithram"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printy(self):
        print(self.name)
        print(self.age)
        print(self.schoolname)

    @classmethod
    def change_school(cls, schoolname):
        cls.schoolname = schoolname


ad = Dep("Samyak", 21)

ad.printy()  # samayak 21 choithram

ad.change_school("Medicaps")

ad.printy()  # samyak 21 medicaps

m = Dep("ram", 22)
m.printy()
print(m.schoolname)  # ram 22 medicaps
# means the classvaribale is changed now


"""sattoc methods"""


class fx:
    @staticmethod
    def addi(x, y):
        return x + y


print(fx.addi(23, 20))


"""DUNDER METHODS"""
"""__init___():it is constructor only
  __str___():it give human friendly representation withoyt it ir will only be objevtcrepresentation"""


"""Str and its uses"""


class abc:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f"ello my name is {self.name} and age sis {self.age}")


ab = abc("samyak", 21)


"""repr:used for friendly representation of the objects """


class and1:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"(ame:{self.name!r},age{self.age!r})"


df = and1()
print(repr(df))
# output will be( name:samyak","age" :22)


"""len:for the length representations"""


class leg:
    def add(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


aso = leg()
aso.add(["sam", "sar", "dujb"])
print(len(aso))


"""Without appropriate equality behavior, two separate objects are not automatically
 considered equal merely because their attributes match"""
"""E__eq__"""


class Abc:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


sss = Abc("sam", 21)
s33 = Abc("sam", 21)

print(sss == s33)
