import Input, Output, Solver
import time


print("=====PySat=====")
board = Input.input_board("input.txt")
Output.print_board(board)
print()

start_time_1 = time.time()
result = Solver.solve_board(board)
end_time_1 = time.time()

Output.assign_result(board, result)
Output.print_board(board)

elapsed_time1 = end_time_1 - start_time_1
print("Elapsed time:", elapsed_time1, "seconds")

print("=====DPLL Algorithm=====")
DPLL_board = Input.input_board("input.txt")
Output.print_board(DPLL_board)
print()

start_time_2 = time.time()
dpll_result = Solver.solve_board_dpll(DPLL_board)
end_time_2 = time.time()

Output.assign_result(DPLL_board, dpll_result)
Output.print_board(DPLL_board)

elapsed_time3 = end_time_2 - start_time_2
print("Elapsed time:", elapsed_time3, "seconds")

if board == DPLL_board:
    print("True")
else:
    print("False")
    
    
# print("=====Brute-Force=====")
# # Get Board from file input 
# Brute_Board = Input.input_board("input.txt")
#print()

# # Solve problem
# start_time_3 = time.time()
# brute_force_result = Solver.brute_force(Brute_Board)
# end_time_3 = time.time()
# elapsed_time_3 = end_time_3 - start_time_3

# # Print result
# if brute_force_result:
#     Output.print_board(brute_force_result)
# else:
#     print("No Solution.")
# print("Elapsed time:", elapsed_time_3, "seconds")


