import numpy as np


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = np.zeros((self.n, self.m))

    def get_element(self, i, j):
        if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0]):
            return self.matrix[i][j]
        else:
            return None

    def set_element(self, i, j, value):
        if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0]):
            self.matrix[i][j] = value

    def transpose(self):
        return np.transpose(self.matrix)

    def multi_matrix(self, matrix2):
        if len(self.matrix[0]) == len(matrix2):
            return self.matrix @ matrix2
        else:
            return None

    def apply_operation(self, operation):
        new_matrix = np.copy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                new_matrix[i][j] = operation(self.matrix[i][j])
        self.matrix = new_matrix
        print(self.matrix)
