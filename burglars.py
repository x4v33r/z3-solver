# coding: utf-8
from z3 import *

################################# Burglars ##################################
# create the solver
solver = Solver()

#############################################################################
# (1) Ed: "Fred did it, and Ted is innocent".
# (2) Fred: "If Ed is guilty , then so is Ted".
# (3) Ted: "Im innocent, but at least one of the others is guilty".
#############################################################################

# TODO Create boolean variables for each of the culprits
# TODO Add constraints to the solver representing the statements from above

# Hint: The statement of a culprit should be true if and only if he is not guilty!

Ed = Bool("Ed")
Fred = Bool("Fred")
Ted = Bool("Ted")

solver.add(Implies(Not(Ed), And(Fred, Not(Ted))))

solver.add(Implies(Not(Fred), Implies(Ed, Ted)))

solver.add(Implies(Not(Ted), And(Not(Ted), Or(Ed, Fred))))


res = solver.check()
if res != sat:
    print("unsat")
    sys.exit(1)

print(solver)
m = solver.model()
for d in m.decls():
    print("%s -> %s" % (d, m[d]))

print("\n" + str(m))
