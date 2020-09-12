class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self,nbr,wt=0):
        if nbr not in self.connectedTo.keys():
            self.connectedTo[key] = wt
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(Self):
        return self.id
    
    def getweight(self,nbr):
        return self.connectedTo[nbr]
    
    def __str__self):
        return self.id+"connected to"+ str(x.id for x in self.connectedTo)

class Graph:
    def __int__(self):
        self.vertList = {}
        self.numvertices = 0
    
    def addVertex(self,key):
        self.numvertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self,f,t,w):
        if f not in self.vertList:
            newVertex = Vertex(f)
        if t not in self.vertList:
            newVertex = Vertex(t)
        self.vertlist[f].addNeighbor(self.vertList[t],wt=9)

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
