import Graph
import DFS

vals = Graph.createGraph(7, 0)
print vals[0]
matrix = vals[0]
nodeList = vals[1]
DFS.DFS(nodeList)
transposedVals = Graph.transpose(nodeList, matrix)
transposedMatrix = transposedVals[0]
transposedNodeList = transposedVals[1]
print transposedMatrix
scclist = DFS.strongly_connected(transposedNodeList)
print scclist



