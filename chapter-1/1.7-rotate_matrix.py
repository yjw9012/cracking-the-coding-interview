def rotate_matrix(matrix):
    if len(matrix) == 0:
        return matrix
    if len(matrix) != len(matrix[0]):
        raise Exception("Matrix is not valid for rotation")

    dimension = len(matrix)
    for i in range(dimension-1):
        start_idx = (0, i)
        tmp = matrix[start_idx[0]][start_idx[1]]
        for j in range(4):
            next_idx = (start_idx[1], dimension-1-start_idx[0])
            num = tmp
            tmp = matrix[next_idx[0]][next_idx[1]]
            matrix[next_idx[0]][next_idx[1]] = num
            start_idx = next_idx


if __name__ == "__main__":

    matrix = [[0] * 3 for i in range(3)]

    matrix[0][1] = 1
    matrix[0][2] = 2
    matrix[1][0] = 3
    matrix[1][1] = 4
    matrix[1][2] = 5
    matrix[2][0] = 6
    matrix[2][1] = 7
    matrix[2][2] = 8

    rotate_matrix(matrix)

    print(matrix)

    matrix = []
    print(matrix)

    matrix = [[0] * 2 for i in range(4)]
    rotate_matrix(matrix)
