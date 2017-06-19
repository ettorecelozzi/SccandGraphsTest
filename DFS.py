# coding=utf-8
time = 0
nodeAndTimes = {}


def DFS(nodeList):
    for node in nodeList:
        node.setParent(None)
    for node in nodeList:
        if node.getColor() == "white":
            DFSVisit(node)


def DFSVisit(u):
    global time
    time += 1
    u.setD(time)
    u.setColor("gray")
    for node in u.getSons():
        if node.getColor() is "white":
            node.setParent(u)
            DFSVisit(node)
    u.setColor("black")
    time += 1
    u.setEndTime(time)
    nodeAndTimes[time] = u  # dizionario per salvare il tempo di fine e il nodo corrispondente


def strongly_connected(nodes):
    scc_list = []

    def dfswrap(node):
        scc = []

        def Scc(u):
            u.setColor("gray")
            for node in u.getSons():
                if node.getColor() is "white":
                    node.setParent(u)
                    Scc(node)
            u.setColor("black")
            scc.append(u)  # lista dichiarata nel wrap

        # siccome devo salvare il valore ad ogni ricorsione sono costretto a creare un contenitore
        # che salva ogni volta il valore nella lista
        Scc(node)
        return scc

    def DFStrasposed(nodelist):
        # non scriviamo i tempi sul grafo trasposto perchè usiamo i tempi del grafo non trasposto
        global nodeAndTimes
        reversenode = []
        for endtime, node in reversed(sorted(nodeAndTimes.iteritems())):
            reversenode.append(node)  # lista contenente i nodi da seguire in ordine decrescente
        for node in nodelist:
            node.setColor("white")
        for node in reversenode:
            if node.getColor() == "white":
                scc_list.append(dfswrap(node))

    DFStrasposed(nodes)
    return scc_list
