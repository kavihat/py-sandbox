# ZERO  MATRIX

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
zero = []
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            zero.append(j)
            zero.append(i)
while zero:
    x = zero.pop()
    y = zero.pop()
    for j in range(n):
        matrix[x][j] = 0
    for i in range(m):
        matrix[i][y] = 0

print(matrix)
