# coding=utf-8
import Node
import AdjacencyMatrix
import numpy as np


def createGraph(vertices, edges):  # nota edges <= vertices^2
    nodeList = []
    for i in range(0, vertices):
        nodeList.append(Node.Node())
    adjMatrix = AdjacencyMatrix.createMatrix(vertices, edges)
    # adjMatrix=np.array([[0,1,0],[0,0,1],[1,0,0]])
    for i in range(0, vertices):
        for j in range(0, vertices):
            if adjMatrix[i][j] == 1:
                nodeList[i].addSon(nodeList[j])
    returnList = [adjMatrix, nodeList]
    return returnList


# è necessaria la lista dei nodi perchè voglio fare il grafico trasposto. Mi serve che la DFS trasposed
# operi sui nodi del grafico di partenza, quindi non devo cambiare gli indirizzi in memoria. I nodi di partenza
# e quelli del grafo trasposto devono essere collegati per far si che la mia DFS transposed percorra gli stessi
# cammini, pertanto elimino i figli del grafo di partenza per sostituirli con quelli del grafo trasposto
def transpose(nodelist, matrix):
    for i in range(0, len(nodelist) - 1):
        nodelist[i].setSon()
    transposedMatrix = AdjacencyMatrix.traspose(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if transposedMatrix[i][j] == 1:
                nodelist[i].addSon(nodelist[j])
    returnList = [transposedMatrix, nodelist]
    return returnList
