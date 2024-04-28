import Utils

def assign_result(board, result):    
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
    height = len(board)
    width = len(board[0])
    for r in range(height): # rows   
        for c in range(width): # columns
            print (board[r][c], " ", sep="", end="")  
        print()