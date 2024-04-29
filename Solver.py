import Input, Utils
from pysat.formula import CNF
from pysat.solvers import Glucose3

''' SOLVER '''
def generate_cnf(board, height, width, numbered_list):
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
    return cnf

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
    cnf = generate_cnf(board, height, width, numbered_list)

    # print(cnf.clauses)
    g = Glucose3()
    g.append_formula(cnf.clauses)
    g.solve()
    # print(g.get_model())
    return g.get_model()

'''BRUTE FORCE'''
def checkboard(board, numbered_list):
    for cell in numbered_list:
        r = cell[0]
        c = cell[1]
        height = len(board)
        width = len(board[0])
        neighbors = [
            [r - 1, c - 1], [r - 1, c], [r - 1, c + 1],
            [r, c - 1], [r, c + 1],
            [r + 1, c - 1], [r + 1, c], [r + 1, c + 1]
        ]
        trap_number = 0
        # Count trap number at cell
        for i in neighbors:
            if ((i[0] >= 0 and i[0] < height) and (i[1] >= 0 and i[1] < width)):
                if board[i[0]][i[1]] == 'T':
                    trap_number = trap_number + 1

        # Compare with input
        if (int(board[r][c]) != trap_number):
            return False

    return True

def generate_possible_output(input_matrix, numbered_list):
    """Generate possible output configurations from the input matrix."""
    possible_outputs = []

    n = len(input_matrix)
    m = len(input_matrix[0])

    # Helper function to generate possible configurations recursively
    def generate_configurations(matrix, i, j, result_matrix):
        if result_matrix is not None:
            return result_matrix
        
        if i == n:
            # Check when create each map
            if checkboard(matrix, numbered_list) == True:
                return [row[:] for row in matrix]
            else: 
                return None

        next_i = i if j + 1 < m else i + 1
        next_j = (j + 1) % m

        if matrix[i][j] == '_':
            # Generate two configurations: one with 'G' and one with 'T'
            for cell in ['G', 'T']:
                matrix[i][j] = cell
                result_matrix = generate_configurations(matrix, next_i, next_j, result_matrix)
                matrix[i][j] = '_'
            if result_matrix is not None:
                return result_matrix
        else:
            # Keep the cell value and proceed to the next cell
            result_matrix = generate_configurations(matrix, next_i, next_j, result_matrix)
            if result_matrix is not None:
                return result_matrix
        return result_matrix

    # Start generation from the top-left cell
    return generate_configurations(input_matrix, 0, 0, None)

def brute_force(board):

    numbered_list = Input.get_numbered_cells(board)
    matrix = generate_possible_output(board, numbered_list)
    return matrix


