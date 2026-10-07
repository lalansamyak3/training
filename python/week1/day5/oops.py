"""Inheritance is the parent child relationship parent takes the property of child"""


class base:
    def __init__(self):
        print("parent class constructor invoked")

    def helo(self, age, gender):
        self.age = age
        self.gender = gender

    def printo(self):
        print(self.age)
        print(self.gender)


class child(base):
    def __init__(self):
        super().__init__()

    def rnt(self, age, gender, city):
        super().helo(age, gender)
        self.city = city

    def printo(self):
        super().printo()
        print(self.city)


c = child()
c.rnt(21, "male", "indore")
c.printo()


"""multiple inheritance in python"""


class m1:
    def __init__(self):
        print("base class constructor")

    def imdo(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(self.name)
        print(self.age)


class m2(m1):
    def __init__(self):
        super().__init__()

    def imdo(self, name, age, gender):
        super().imdo(name, age)
        self.gender = gender

    def printing(self):
        super().print()
        print(self.gender)


class m3(m1):
    def __init__(self):
        super().__init__()

    def imdo(self, name, age, gender, city):
        super().imdo(name, age)
        self.gender = gender
        self.city = city

    def print(self):
        super().print()
        print(self.gender)
        print(self.city)


abd = m3()
abd.imdo("samyak", 21, "male", "indore")
abd.print()


"""ABstraction in python"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

"""any class or implementing class which inherits the methods of parent or abstract class
should implement these methods if it is not implementing these methods then error will come"""
"""multiple abstract methods and abstract class can have concrete methods too"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # abstract class can have non abstract methods too as well
    def idn(self):
        print("hiijenjedned")


class child(Vehicle):
    def start(self):
        print("ikmjmkol")

    def stop(self):
        print("lets stop the work now")


c = child()
c.stop()
c.start()
c.idn()

# abstract class ka obj nhi banta h implementing class only we can create object

"""abstract classes can also have constructor too"""


"""abstract properties"""

from abc import ABC, abstractmethod


class omi(ABC):

    @abstractmethod
    def onto(self):
        pass


####################################################################################################################
"""method overriding"""


class Animal:

    def speak(self):
        print("Some sound")


class Dog(Animal):

    def speak(self):
        print("Woof")


dog = Dog()

dog.speak()


####################################################################################################33
"""method overloading"""


class sam:
    def add(self, x=0, y=0, z=0):
        return x + y + z


a = sam()
print(a.add(10, 20))

b = sam()
print(b.add(10, 20, 30))


########################################################################################################
"""composition means one object needs another object to work """

"""car needs an engine to work its a has a relationship"""


class Engine:
    def start(self):
        print("start the engine")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("car started")


car = Car()
car.start()


"""suppose you have order service and payment service and 
its like this  class orderservice(paymentservcice) meands oderservuce is pyament service 
instead oderserviec has patience service """
