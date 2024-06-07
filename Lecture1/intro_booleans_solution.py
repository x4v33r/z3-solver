from z3 import *

a, b = Bools("a b")

solver = Solver()
solver.add(Not(b))
solver.add(Or(a,b))

result = solver.check()
model = solver.model()
print(model)
