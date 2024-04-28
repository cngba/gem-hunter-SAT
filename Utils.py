''' UTILITIES '''
def coords_to_num(row, col, width):
    '''
    Example: A row with 5 elements (0,1,2,3,4);
    cell (2,1) is converted to 2 * 5 + 1 = 11
    '''
    return row * width + col

def coords_to_num_lst(neighbors, width):
    num_lst = []
    for (x, y) in neighbors:
        num_lst.append(coords_to_num(x, y, width))
    return num_lst

def at_most(n, neighbors):
    """
    n is the number of bombs nearby
    neighbors is the list of neighboring cells
    """
    clauses = []

    rows_count = 2 ** len(neighbors)
    for row in range(rows_count):
        bin_representation = '{0:0{len}b}'.format(row, len=len(neighbors))
        bit_count = bin_representation.count("1")
        if bit_count == n + 1:
            """
            Example: There are 2 bombs nearby
            Which means n == 2
            then if bit_count == 3
            then create a clause that n
            """
            clauses.append([-neighbors[i] for i in range(len(neighbors)) if (bin_representation[i] == '1')])

    return clauses

def at_least(n, neighbours):
    clauses = []

    rows_count = 2 ** len(neighbours)
    for row in range(rows_count):
        bin_representation = '{0:0{len}b}'.format(row, len=len(neighbours))
        bit_count = bin_representation.count("1")
        if bit_count == (len(neighbours) - (n - 1)):
            clauses.append([neighbours[i] for i in range(len(neighbours)) if (bin_representation[i] == '1')])

    return clauses

def get_cell_constraints(cell_num, neighbours):
    "Only use for numbered cells"
    if cell_num == 0:
        return [[-neighbours[i]] for i in range(len(neighbours))]

    most = at_most(cell_num, neighbours)
    least = at_least(cell_num, neighbours)
    return most + least

