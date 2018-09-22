class Vertex(object):

    def __init__(self,id):
        self.id = id
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + '  connectedTo : ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
            return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph(object):

    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def addVertext(self,id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertexList[id] = newVertex
        return  newVertex

    def getVertex(self,n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def getVertices(self):
        return self.vertexList.keys()

    def addEdge(self,f,t,w):
        if f not in self.vertexList:
            self.addVertext(f)
        if t not in self.vertexList:
            self.addVertext(t)
        self.vertexList[f].addNeighbor(self.vertexList[t],w)

    def __iter__(self):
        return iter(self.vertexList.values())


g = Graph()
for i in range(1,11):
    g.addVertext(i)

g.addEdge(1,2,0)
g.addEdge(1,3,0)
g.addEdge(3,4,0)
g.addEdge(5,6,0)

for vertex in g:
    print(vertex)
    print(vertex[x] for x in vertex.getConnections())
    print("")