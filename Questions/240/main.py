def search_matrix(matrix: list[list[int]], target: int) -> int:
    m, n = len(matrix), len(matrix[0])

    # initialize a position at the top right of the matrix
    x, y = 0, n - 1
    while x <= m and y >= 0:
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            x -= 1
        else:
            y += 1

    return False



#matrix = [
# [1,4,7,11,15],
# [2,5,8,12,19],
# [3,6,9,16,22],
# [10,13,14,17,24],
# [18,21,23,26,30]], target = 5
        