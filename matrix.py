from copy import  deepcopy
import numpy as np


class Matrix():
    def __init__(self, a=[]):
        if not self.size_validation(a):
            raise ValueError('Matrix size validation error')
        self.elements = deepcopy(a)
        self.row_size = len(a)
        self.col_size = len(a) and int(type(a[0]) == list) and len(a[0])

    @staticmethod
    def size_validation(matrix):
        if matrix == []:
            return True
        try:
            row_size = len(matrix[0])
            for row in matrix[1:]:
                if row_size != len(row):
                    return False
        except (IndexError, TypeError):
            return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('second matrix is not Matrix instance')
        if not (self.row_size == other.row_size and self.col_size == other.col_size):
            raise ValueError('Matrix\'s lengths is not equal')
        m = Matrix([])
        for i, _ in enumerate(self.elements):
            m.elements.append([])
            for j, __ in enumerate(self.elements[i]):
                m.elements[i].append(self.elements[i][j] + other.elements[i][j])
        return m

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('second matrix is not Matrix instance')
        if not (self.col_size == other.row_size):
            raise ValueError('Can\'t multiply matrix\'s')
        p = Matrix([])
        for k, _ in enumerate(self.elements):
            gum = 0
            p.elements.append([])
            for i, ___ in enumerate(self.elements):
                for j, __ in enumerate(self.elements[i]):
                    gum = gum + self.elements[k][j] * other.elements[j][i]
                p.elements[k].append(gum)
        return p

    def trans(self):
        for i in enumerate(self.elements):
            for j in enumerate(self.elements[i]):
                k = self.elements[i][j]
                self.elements[i][j] = self.elements[j][i]
                self.elements[j][i] = k
        return Matrix(self.elements)

    def determinant(self):
        # determinant = self.elements[0][0] * self.elements[1][1] * self.elements[2][2] + self.elements[1][0] * self.elements[2][1] * self.elements[0][2] + self.elements[0][1] * self.elements[1][2] * self.elements[2][0]
        # return determinant
        det = np.linalg.det(self.elements)
        return det

    def __str__(self):
        matrix_string = ''
        for i in self.elements:
            matrix_string += ' '.join([str(j) for j in i]) + '\n'
        return matrix_string


    # def __repr__(self):
    #     matrix_string = ''
    #     for i in self.a:
    #         matrix_string + ' '.join([str(j) for j in i]) + '\n'
    #     return matrix_string


if __name__ == '__main__':
    m = Matrix([])

    n = Matrix([[1, 1, 0], [5, 1, 0], [0, 1, 1]])
    f = Matrix([[0, 2, 0], [0, 2, 0], [0, 2, 0]])
    # r = n * f
    # print(r)

    print(n.determinant())