neighbours = [2,3,4]
n = 2
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
            Example: There are 3 bombs nearby
            Which means n == 3
            if bit_count == 4 
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

def get_cell_constraints(n, neighbours):
    if n == 0:
        return [[-neighbours[i]] for i in range(len(neighbours))]

    most = at_most(n, neighbours)
    least = at_least(n, neighbours)
    return most + least

data = get_cell_constraints(n, neighbours)


for i in data:
    print(i)