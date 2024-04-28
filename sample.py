from pysat.solvers import Glucose3

def solve_sat_problem():
    # Initialize the solver
    solver = Glucose3()

    # Add clauses (logical statements) to the solver
    solver.add_clause([1,2])
    solver.add_clause([1,2,3])
    solver.add_clause([2,3])

    # Solve the problem
    if solver.solve():
        # If a solution is found, get the solution
        solution = solver.get_model()
        print("Satisfiable! Solution:", solution)
    else:
        print("Unsatisfiable!")

if __name__ == "__main__":
    solve_sat_problem()
