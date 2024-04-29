import random

#số T + số G
NUM_T_G = 25
#Kích thước ma trận
N = 11
# Khởi tạo ma trận 11x11 với tất cả các ô trống
matrix = [['_'] * N for _ in range(N)]
lst_domain = []
# Đặt ngẫu nhiên các vị trí T và G trên ma trận
for _ in range(NUM_T_G): 
    i, j = random.randint(0, N-1), random.randint(0, N-1)
    while matrix[i][j] != '_':
        i, j = random.randint(0, N-1), random.randint(0, N-1)
    matrix[i][j] = random.choice(['T', 'G'])
    lst_domain.append((i, j))

lst = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (matrix[i][j] == '_'):
            lst.append((i, j))

for row in matrix:
    for index, element in enumerate(row):
        if index == len(row) - 1:  # Kiểm tra nếu là phần tử cuối cùng trong hàng
            print(element, end=' ')  # Không thêm dấu '|' sau phần tử cuối cùng
        else:
            print(element + ',', end=' ')  # Thêm dấu '|' sau các phần tử khác
    print()  # Xuống dòng sau mỗi hàng
    
for cell in lst:
    r = cell[0]
    c = cell[1]
    height = len(matrix)
    width = len(matrix[0])

    neighbors = [
        [r - 1, c - 1], [r - 1, c], [r - 1, c + 1],
        [r, c - 1], [r, c + 1],
        [r + 1, c - 1], [r + 1, c], [r + 1, c + 1]
    ]
    trap_number = 0
    for i in neighbors:
        if ((i[0] >= 0 and i[0] < height) and (i[1] >= 0 and i[1] < width)):
            if matrix[i[0]][i[1]] == 'T':
                trap_number = trap_number + 1
    matrix[r][c] = str(trap_number)
    
print("Output")
for row in matrix:
    for index, element in enumerate(row):
        if index == len(row) - 1:  # Kiểm tra nếu là phần tử cuối cùng trong hàng
            print(element, end=' ')  # Không thêm dấu '|' sau phần tử cuối cùng
        else:
            print(element + ',', end=' ')  # Thêm dấu '|' sau các phần tử khác
    print()  # Xuống dòng sau mỗi hàng


for cell in lst_domain:
    r = cell[0]
    c = cell[1]
    matrix[r][c] = '_'

print("Input")
for row in matrix:
    for index, element in enumerate(row):
        if index == len(row) - 1:  # Kiểm tra nếu là phần tử cuối cùng trong hàng
            print(element, end=' ')  # Không thêm dấu '|' sau phần tử cuối cùng
        else:
            print(element + ',', end=' ')  # Thêm dấu '|' sau các phần tử khác
    print()  # Xuống dòng sau mỗi hàng