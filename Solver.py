import Input, Utils
from pysat.formula import CNF

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




def solve_board(board):
    '''
    Only one epoch. This is much more simple than conventional Minesweeper
    '''    
    numbered_list = Input.get_numbered_cells(board)
    cnf = CNF()
    for cell in numbered_list:
        cnf.extend(solve_cell(board, cell))


''' MAIN EXE '''
board = Input.input_board("input.txt")
empty_list = Input.get_empty_cells(board)
