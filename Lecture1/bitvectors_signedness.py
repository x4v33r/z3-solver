from z3 import *

solver = Solver()

bvX  = BitVec("bvX", 8)

solver.add(bvX + 1 < bvX - 1)
print(f"Current 'state' of the solver:\n {solver.sexpr()}")
input("Hit Enter.")
result = solver.check()
print(result)
if result == sat:
    print("=== Model ===")
    for var in solver.model().decls():
        print(f"M: {var}: int:{solver.model()[bvX].as_long()}, binary:{bin(solver.model()[bvX].as_long())} \t | type: {type(solver.model()[var])}")
    print("=============")
























solver.add(BVAddNoOverflow(bvX, 1, True))
solver.add(BVSubNoUnderflow(bvX, 1, True))
input("Hit Enter.")
print(f"Current 'state' of the solver:\n {solver.sexpr()}")
input("Hit Enter.")
result = solver.check()
print(result)
if result == sat:
    print("=== Model ===")
    for var in solver.model().decls():
        print(f"M: {var}: int:{solver.model()[bvX].as_long()}, binary:{bin(solver.model()[bvX].as_long())} \t | type: {type(solver.model()[var])}")
    print("=============")
