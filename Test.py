import Graph
import random
from timeit import default_timer as timer


def genrandom():
    nodi = random.randint(1, 10)
    archi = random.randint(1, 10)
    valori = [nodi, archi]
    return valori


def riempigrafi(nodi):
    j = 0
    endit = nodi * nodi
    while j <= endit:
        start = timer()
        Graph.createGraph(nodi, j)
        j += 1
        if j == endit / 2:
            fine = timer()
            print "Tempo grafo completo a meta:",
            print fine - start
    end = timer()
    return start, end


def test():
    i = 2
    while i <= 20:
        tst = riempigrafi(i)
        print tst[1] - tst[0]
        i += 1


test()
