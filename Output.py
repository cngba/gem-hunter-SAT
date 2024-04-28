import Utils

def assign_result(board, result): 
    "Assign traps and gems into empty cells"
    if (result == None):
        print("No Solution")
        return
    height = len(board)
    width = len(board[0])
    for i in range(height):
        for j in range(width):
            if board[i][j] == '_':
                cell_num = Utils.coords_to_num(i, j, width)
                if cell_num in result:
                    board[i][j] = 'T'
                elif cell_num * (-1) in result:
                    board[i][j] = 'G'

def print_board(board):
    "Print board without any commas, brackets, for illustration"
    height = len(board)
    width = len(board[0])
    for r in range(height): # Rows   
        for c in range(width): # Columns
            print (board[r][c], " ", sep="", end="")  
        print()