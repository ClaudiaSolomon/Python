# 9
def heights(seat_matrix):
    list_tuples = []
    for i in range(1, len(seat_matrix)):
        for j in range(0, len(seat_matrix[0])):
            if seat_matrix[i][j] < seat_matrix[i - 1][j]:
                list_tuples.append((i, j))
    return list_tuples


print(heights([[1, 2, 3, 2, 1, 1],
               [2, 4, 4, 3, 7, 2],
               [5, 5, 2, 5, 6, 4],
               [6, 6, 7, 6, 7, 5]]))
