def transpose(matrix):
    row,cols = len(matrix),len(matrix[0])
    result = [[0 for i in range(row)] for j in range(cols)]
    for i in range(row):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
matrix = [[1,2,3],[4,5,6]]
transposed = transpose(matrix)
print(transposed)
