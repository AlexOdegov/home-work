def get_matrix (n,m,value):
    matrix = []
    for i in range(n):
        strings = []
        matrix.append(strings)
        for j in range(m):
            strings.append(value)
    return matrix

result1 = get_matrix(4, 5,7)
result2 = get_matrix(6, 3, 32)
result3 = get_matrix(5, 4, 17)
print(result1)
print(result2)
print(result3)


