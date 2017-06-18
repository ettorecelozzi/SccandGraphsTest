import Graph
from timeit import default_timer as timer


def riempigrafi(nodi):
    j = 0
    endit = nodi * nodi
    while j <= endit:
        start = timer()
        Graph.createGraph(nodi, j)
        j += 1
        if j == endit / 2:
            fine = timer()
            print "Grafo con", nodi, "nodi"
            print "Tempo grafo con", j, "archi:",
            print fine - start
    end = timer()
    return start, end


def test(numnodi):
    i = 2
    while i <= numnodi:
        tst = riempigrafi(i)
        print "Tempo grafo completo:",
        print tst[1] - tst[0]
        print " "
        i += 1


