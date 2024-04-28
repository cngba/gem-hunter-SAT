from pysat.solvers import Glucose3
from pysat.formula import CNF
def solve_sat_problem():
    # Initialize the solver
    solver = Glucose3()

    # Add clauses (logical statements) to the solver
    cnf = CNF()
    clauses = [
        [-7, -8], [7, 8],
        [-8, -9], [-7, -9], [-7, -8], [7, 8, 9],
        [-8, -9], [8, 9],
        [-12], [-13], [-14],
        [-17], [-18], [-19]
    ]
    cnf.extend(clauses)
    solver.append_formula(cnf.clauses)
    # Solve the problem
    if solver.solve():
        # If a solution is found, get the solution
        solution = solver.get_model()
        print("Satisfiable! Solution:", solution)
    else:
        print("Unsatisfiable!")

if __name__ == "__main__":
    solve_sat_problem()
