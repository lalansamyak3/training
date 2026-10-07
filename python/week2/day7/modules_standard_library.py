from dataclasses import fields

import python.week2.day7.day7 as day7

print(day7.add(2, 3))
print(day7.sub(12, 34))

import python.week2.day7.day7 as d

print(d.add(12, 22))
print(d.sub(23, 33))
# to import the specific only
from python.week2.day7.day7 import add

print(add(12, 22))

# to import everything which is there in the day7 module
from python.week2.day7.day7 import *

print(add(22, 33))
print(add(23, 32))


import math as m

print(m.ceil(10.33))
print(m.floor(33.334))
print(m.pow(2, 3))
print(m.fabs(-33))
print(m.fsum(2, 3))
print(m.factorial(13))
print(m.isqrt(12))
print(m.fmod(10))
print(m.isclose(2, 2.1))
print(m.isfinite(12))
print(m.isfinite(10 / 0))
print(m.log10(200))
from datetime import date, datetime, time, timedelta

print(datetime(12))
print(date)
now = daytime.now()
print(now)
today = date.today()
print(today)
# creating date ,time and datetime
d = date(2026, 9, 10)
t = time(14, 30, 0)


###############################################################
# calender module
import calender

print(calender.month(2026, 1))
print(calender.calender(2026))
# to check leap year
print(calender.isleap(2026))
# to see the week day which dyay of the wek isit
print(calender.weekday(2026, 6, 24))
print(calender.month_name[9])
print(calender.day_name[3])
##########################################################################################################
"""COLLECTIONS """
# used in variety of purposes like 1)counter to count no of words
from collections import Counter

l1 = ["a", "b", "d", "f", "f"]
z = Counter(l1)
print(z)
print(z.most_common(1))
print(z["a"])
z.update(["a", "z"])
print(z.total())
s1 = "samyak"
print(Counter(s1))

# arithmatic between counters
c1 = Counter(a=3, b=2)
c2 = Counter(a=2, b=2)
print(c1 - c2)
print(c1 + c2)
print(c1 & c2)
print(c1 | c2)
###########################################################################################################
"""collections part 2) default dictionary """
from collections import defaultdict

d = defaultdict(list)
# grouping the iteams
for name, dep in [("samyak", "english"), ("raj", "maths"), ("shaam", "english")]:
    d[dep].append(name)
# Counting manually (like Counter)
d = defaultdict(int)
for word in ["a", "b", "a"]:
    d[word] += 1
##############################################################################################3
# 2)ordered dictionary that maintains the insertion oder
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["n"] = 2
od.move_to_end("a")
od.move_to_end("b", last=False)
print(od.popitem())
print(od.keys())
print(od.values())
print(od.items())
od.update({"a": 12})
od.clear()
od.copy()
###############################################################################################3
# 3) name tupple help us to get the elements by name not by position like
"""normally we have t1=(2,3,4) and print(t1[0]) accesing the elements by the positions 
but what if we truy to acces the element usig the keys or name 
lightweight immuatbel objects with the named fie;ld 
"""

from collections import namedtuple

Point = namedtuple("point", ["x", "y"])
p = Point(3, 4)
print(p.x)
print(p.y)

p[0], p[1]
x, y = p
x._asdict()
p.fields()
######################################################################################################
# 4) dequeue :fast append/pop from both the ends
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(5)
dq.pop()
dq.popleft()
# append is used to add th eleemnet at the right side appendleft to add element to left side
# ppop() remove elements from thre right side and popleft() is used to remove the element from the
# left side


# roatte the elements of the queue
# roatete the elemetsnsby 1
dq.rotate(1)
dq.rotate(-1)

recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
print(recent)

"""used for fast insertion and fast deletion """


##################################################################################################
# chainmap ciombine multiple dict into one view
from collections import ChainMap

dict1 = {"name": "samyak", "age": 21}
dict2 = {
    "name": "raj",
}
c = ChainMap(dict1, dict2)
print(c["name"])
print(c["age"])
c.maps()

"""soplves the floating point problem by0.1+0.2=0.3 by using base 10 arithmatic essential for money calculations
"""

from decimal import Decimal, getcontext, localcontext, ROUND_HALF_UP

d1 = Decimal("0,1")
d2 = Decimal("0.2")
print(d1 + d2)

# d3=Decimal(0.3) will giv ana eror in this case
"""get_context get the current thread contexct """

d1.exp()
d1.sqrt()
d1.log10()
d1.as_tuple()


"""Represents numbers as exact numerator/denominator pairs — no rounding error at all, unlike float or even Decimal (which is still base-10 finite precision).
"""
from fractions import Fraction

f1 = Fraction(1, 3)
print(f1.numerator)
# auto reduces to ythe lowest term
print(f1.denominator)
f2 = Fraction("1.5")
f3 = Fraction(0.5)
print(f1.as_integer_ratio())
###############################################################################3
import random

print(random.random())
print(random.randint(23))
print(random.randrange(1, 200))
print(random.uniform([0, 1]))  # random float in -0 and 1
print(random.randbytes(2))
l1 = [1, 2, 3, 2, 4]
print(random.choice(l1))
print(random.shuffle(l1))
print(random.sample(l1))
############################################################################################3
"""Statics ke luye """
import statistics

data = [1, 2, 3, 4, 4]
statistics.mean(data)
statistics.fmean(data)
statistics.median(data)
statistics.harmonic_mean(data)
statistics.median_high(data)
statistics.median_low(data)
statistics.mode(data)
statistics.multimode(data)
