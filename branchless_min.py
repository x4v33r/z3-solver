# coding: utf-8
import os, sys
from z3 import *

# Create an instance of a z3 solver
solver = Solver()
# Declare z3 variables for the needed BitVectors

x = BitVec("x", 32)
y = BitVec("y", 32)
tmp = BitVec("tmp", 32)

min_bithack = BitVec("min_bithack", 32)
min_expected = BitVec("min_expected", 32)


solver.add(tmp == If(x < y, BitVecVal(1, 32), BitVecVal(0, 32)))
solver.add(min_bithack == y ^ ((x ^ y) & -tmp))


solver.add(min_expected == If(x < y, x, y))


# Check for equivalence
solver.add(min_bithack != min_expected)

# Check and print the result.
result = solver.check()
print(result)
if result == sat:
    print(solver.model())
