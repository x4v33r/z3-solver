# coding: utf-8
import os, sys
import time
from z3 import *

# TODO: Check Equivalence of
# - p -> q
# - !p | q

# create the solver
solver = Solver()




result = solver.check()
print(solver.sexpr())
print(result)


