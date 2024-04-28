def input_board(filename):
    # Open the file
    with open(filename, 'r') as file:
        # Initialize an empty list to store the lists of numbers
        board = []
        
        for line in file:
            raw_items = line.strip().split(',')
            
            # Convert placeholders to characters and convert other elements to integers
            cell = [item.strip() for item in raw_items]
            
            # Append the list of numbers to the main list
            board.append(cell)
    return board

def get_empty_cells(board):
    lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == '_'):
                lst.append((i, j))
    return lst

def get_numbered_cells(board):
    lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j].isnumeric()):
                lst.append((i, j))
    return lst

'''# Print the list of lists
# Define a list of lists
num_list = input_board('input.txt')
# Iterate over each sublist in the list of lists
for sublist in num_list:
    # Iterate over each element in the sublist
    for element in sublist:
        print(element, end=" ")  # Print the element, end with a space to print on the same line
    print()  # Move to the next line after printing all elements of the sublist

print(get_empty_cells(num_list))'''

