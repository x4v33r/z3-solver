#!/usr/bin/python
from z3 import *

x = BitVec('x', 32)
y = BitVec('y', 32)

s = Solver()
s.add(Distinct(((y & x)* -2) + (y + x), x^y))

result = s.check()
print(result)
if result == sat:
    print(s.model())


### A 'different' way ###

s = Solver()
l = (y & x)*-2 + (y+x)
r = x^y
s.add(Distinct(l, r))

result = s.check()
print(result)
if result == sat:
    print(s.model())
