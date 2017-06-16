import numpy as np
import random


def createMatrix(vertices, edges):
    matrix = np.zeros([vertices, vertices], dtype=int)
    for i in range(0, edges):
        r = random.randint(0, vertices - 1)
        c = random.randint(0, vertices - 1)
        while matrix[r][c] == 1:
            r = random.randint(0, vertices - 1)
            c = random.randint(0, vertices - 1)
        matrix[r][c] = 1
    return matrix


def traspose(matrix):
    newMatrix = np.transpose(matrix)
    return newMatrix
