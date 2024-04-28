import Input, Utils
from pysat.formula import CNF
from pysat.solvers import Glucose3
''' SOLVER '''
def solve_cell(board, cell):
    r = cell[0]
    c = cell[1]
    width = len(board[0])

    neighbors = [
        [r-1,c-1], [r-1,c], [r-1,c+1],
        [r,c-1], [r,c+1],
        [r+1,c-1], [r+1,c], [r+1,c+1]
    ]
    neighbors_ids = Utils.coords_to_num_lst(neighbors, width)
    # print(f"Width: {width}")
    # print(f"Cell: {cell}")
    # print(f"Value: {board[r][c]}")
    # print(f"Neighbors: {neighbors_ids}")
    clauses = Utils.get_cell_constraints(int(board[r][c]), neighbors_ids)

    clauses.append([-Utils.coords_to_num(r, c, width)])
    print(clauses)
    return clauses


def solve_board(board):
    '''
    Only one epoch. This is much more simple than conventional Minesweeper
    '''    
    height = len(board)
    width = len(board[0])

    numbered_list = Input.get_numbered_cells(board)
    cnf = CNF()
    for c in range(width + 2):
        cnf.append([-Utils.coords_to_num(0, c, width)])
        cnf.append([-Utils.coords_to_num(height + 1, c, width)])

    for r in range(height + 2):
        cnf.append([-Utils.coords_to_num(r, 0, width)])
        cnf.append([-Utils.coords_to_num(r, width + 1, width)])

    for cell in numbered_list:
        cnf.extend(solve_cell(board, cell))

    g = Glucose3()
    g.append_formula(cnf.clauses)
    g.solve()
    return g.get_model()

''' MAIN EXE '''
board = Input.input_board("input.txt")
print(board)
print()
empty_list = Input.get_empty_cells(board)

print(empty_list)
print(solve_board(board))