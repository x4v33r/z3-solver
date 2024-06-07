from z3 import *

a, b = Bools("a b")

solver = Solver()
solver.add(Not(a))
solver.add(Or(a,b))

#solver.add(And(Not(a), Or(a,b)))

result = solver.check()
print(result)
model = solver.model()
print(model)
#for var in model.decls():
#    print(f"{var}: {model[var]}  \t(:{type(model[var])})")

