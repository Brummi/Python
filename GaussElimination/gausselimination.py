def pivot(matrix, result, n):
    n_t = n
    for i in range(n, len(matrix)):
        if abs(n) > matrix[n_t][n]:
            n_t = i
    tmp = matrix[n]
    matrix[n] = matrix[n_t]
    matrix[n_t] = tmp
    tmp = result[n]
    result[n] = result[n_t]
    result[n_t] = tmp
    return matrix, result


def mulList(l, s):
    return [x*s for x in l]


def addList(l0, l1):
    tmp = []
    for i in range(len(l0)):
        tmp.append(l0[i] + l1[i])
    return tmp


def gaussElimination(matrix, result):
    for j in range(len(matrix)):
        matrix, result = pivot(matrix, result, j)
        scale = 1/matrix[j][j]
        matrix[j] = mulList(matrix[j], scale)
        result[j] = result[j] * scale

        for i in range(j+1, len(matrix)):
            result[i] = result[i] - result[j] * matrix[i][j]
            matrix[i] = addList(matrix[i], mulList(matrix[j], -1*matrix[i][j]))

    for j in range(1, len(matrix)):
        for i in range(j):
            result[i] = result[i] - result[j] * matrix[i][j]
            matrix[i] = addList(matrix[i], mulList(matrix[j], -1*matrix[i][j]))

    return result
