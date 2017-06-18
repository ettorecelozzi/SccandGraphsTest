import Graph
import DFS
import Test

vals = Graph.createGraph(7, 0)
matrix = vals[0]
nodeList = vals[1]
DFS.DFS(nodeList)
transposedVals = Graph.transpose(nodeList, matrix)
transposedMatrix = transposedVals[0]
transposedNodeList = transposedVals[1]
scclist = DFS.strongly_connected(transposedNodeList)
print scclist
numnodi = input("Inserisci numero massimo nodi:")
Test.test(numnodi)



