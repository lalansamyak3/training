x = 100


def printi():
    y = 200
    print(x)
    print(y)


printi()


"""local scope"""


def prio():
    f = 20
    print(f)


prio()


"""global scope is here """
e = 233


def add():
    print(e)


add()


"""localvs global"""


x = 10


def oop():
    x = 23
    print(x)


oop()
print(x)
# 23
# 10
# see the behaviour above


"""PYTHON SEARCHES FOR VARIBALE USING LEGB RUle"""
"""l:loaclly python finds it locally'
e:enclosing nested functions if doesnt have locally searches in netsed functions 
g:if dont find loaclly or nested then search gloablly
b=build in if not found anywhere uses built in to fuind it """


f1 = 100


def pu():
    f = 300

    def inner():
        f = 23
        print(f)


pu()


"""non local means creating a varibale from enclosing function instead pf creating a new local """
