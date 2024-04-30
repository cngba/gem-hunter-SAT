import Input, Output, Solver
import time
board = Input.input_board("input.txt")
Output.print_board(board)

print()

#Cong
print("=====PySat=====")
start_time_1 = time.time()
result = Solver.solve_board(board)
end_time_1 = time.time()
Output.assign_result(board, result)
Output.print_board(board)
elapsed_time = end_time_1 - start_time_1
print("Elapsed time:", elapsed_time, "seconds")


print("=====Brute-Force=====")
# Get Board from file input 
Brute_Board = Input.input_board("input.txt")

# Solve problem
start_time_2 = time.time()
brute_force_result = Solver.brute_force(Brute_Board)
end_time_2 = time.time()
elapsed_time = end_time_2 - start_time_2

# Print result
if brute_force_result:
    Output.print_board(brute_force_result)
else:
    print("No Solution.")
print("Elapsed time:", elapsed_time, "seconds")