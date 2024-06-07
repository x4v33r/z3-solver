# coding: utf-8
import os, sys
import time
from z3 import *


# create the solver
solver = Solver()
a, b = Bools("a b")
l, r = Bools("l r")

solver.add(l == Implies(a, b))
solver.add(r == Or(Not(a), b))
solver.add(Distinct(r,l))

result = solver.check()
print(solver.sexpr())
print(result)

### A different way ###

solver = Solver()
a, b = Bools("a b")
l = Implies(a,b)
r = Or(Not(a),b)
solver.add(Distinct(l,r))
result = solver.check()
print(result)

