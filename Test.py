import Graph
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def riempigrafi(nodi):
    j = 0
    endit = nodi * nodi
    tempi = []
    while j <= endit:
        start = timer()
        Graph.createGraph(nodi, j)
        finearco = timer()
        j += 1
        tempi.append(finearco - start)
        if j == endit / 2:
            fine = timer()
            print "Grafo con", nodi, "nodi"
            print "Tempo grafo con", j, "archi:",
            print fine - start
    end = timer()
    print "Tempo grafo completo:", end - start
    print " "
    return tempi


def test(numnodi):
    i = 2
    while i <= numnodi:
        riempigrafi(i)
        i += 1


def grafici():
    list2 = riempigrafi(2)
    list8 = riempigrafi(8)
    list20 = riempigrafi(20)
    list50 = riempigrafi(50)
    xAxis = []
    for i in range(0, len(list2)):  # contando il numero di tempi registrati ottengo il numero di archi
        xAxis.append(i)
    plt.plot(xAxis, list2)

    plt.xlabel('Number of edges')
    plt.ylabel('Time')
    plt.title("Graph with 2 nodes")
    plt.show()

    xAxis = []
    for i in range(0, len(list8)):
        xAxis.append(i)
    plt.plot(xAxis, list8)

    plt.xlabel('Number of edges')
    plt.ylabel('Time')
    plt.title("Graph with 8 nodes")
    plt.show()

    xAxis = []
    for i in range(0, len(list20)):
        xAxis.append(i)
    plt.plot(xAxis, list20)

    plt.xlabel('Number of edges')
    plt.ylabel('Time')
    plt.title("Graph with 20 nodes")
    plt.show()

    xAxis = []
    for i in range(0, len(list50)):
        xAxis.append(i)
    plt.plot(xAxis, list50)

    plt.xlabel('Number of edges')
    plt.ylabel('Time')
    plt.title('Graph with 50 nodes')
    plt.show()
