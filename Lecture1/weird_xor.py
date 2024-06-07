#!/usr/bin/python
from z3 import *

# TODO: Check for equivalence:
## - (((y & x)*-2) + (y+x))
## -  x^y

s= Solver()



result = s.check()
print(result)
if result == sat:
    print(s.model())
