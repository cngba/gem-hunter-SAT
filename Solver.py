import Input, Utils
from pysat.formula import CNF
from pysat.solvers import Glucose3
''' SOLVER '''
def solve_cell(board, cell):
    r = cell[0]
    c = cell[1]
    height = len(board)
    width = len(board[0])
    # print(f"Height: {height}")
    # print(f"Width: {width}")
    neighbors = [
        [r-1,c-1], [r-1,c], [r-1,c+1],
        [r,c-1], [r,c+1],
        [r+1,c-1], [r+1,c], [r+1,c+1]
    ]
    # print(neighbors)
    empty_neighbors = []
    for i in neighbors:
        if ((i[0] >= 0 and i[0] < height) and (i[1] >= 0 and i[1] < width)):
            if board[i[0]][i[1]] == '_':
                empty_neighbors.append(i)
    # print(empty_neighbors)
    neighbors_ids = Utils.coords_to_num_lst(empty_neighbors, width)

    # print(f"Width: {width}")
    # print(f"Cell: {cell}")
    # print(f"Value: {board[r][c]}")
    # print(f"Neighbors: {neighbors_ids}")
    clauses = Utils.get_cell_constraints(int(board[r][c]), neighbors_ids)

    clauses.append([-Utils.coords_to_num(r, c, width)])
    # print(clauses)
    return clauses


def solve_board(board):
    '''
    Only one epoch. This is much more simple than conventional Minesweeper
    '''    
    height = len(board)
    width = len(board[0])

    numbered_list = Input.get_numbered_cells(board)
    cnf = CNF()

    # Boundary Setup
    for c in range(width + 2):
        cnf.append([-(c + 1)])
        cnf.append([-( (height + 1) * (width + 2) + c + 1)])

    for r in range(height + 2):
        cnf.append([-(r * (width + 2) + 1)])
        cnf.append([-((r + 1) * (width + 2))])

    for cell in numbered_list:
        cnf.extend(solve_cell(board, cell))

    # print(cnf.clauses)
    g = Glucose3()
    g.append_formula(cnf.clauses)
    g.solve()
    # print(g.get_model())
    return g.get_model()




