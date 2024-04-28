import Input, Output, Solver

board = Input.input_board("input.txt")
Output.print_board(board)

print()

result = Solver.solve_board(board)
Output.assign_result(board, result)
Output.print_board(board)