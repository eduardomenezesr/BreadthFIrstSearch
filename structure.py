# Graph Structure and Parser


# The edge structure stores to where this edge is going and the weight of this
# path, as well some methods to get this values
class Edge:
    def __init__(self, to, weight=1):
        self.to = to
        self.weight = weight

    def getTo(self):
        return self.to

    def getWeight(self):
        return self.weight


# The vertex structure stores the name, heuristic, a list of edges, a variable
# that marks if the vertex was visited and the cumulative_weight, as well some
# methods to set and get these values
class Vertex:
    def __init__(self, name=None, h=1):
        self.name = name
        self.h = h
        self.edges = []
        self.visited = False
        self.cumulative_weight = 0

    def getVisited(self):
        return self.visited

    def setVisited(self, value):
        self.visited = value

    def getH(self):
        return self.h

    def setH(self, h):
        self.h = h

    def getEdges(self):
        return self.edges

    def appendEdge(self, edge):
        self.edges.append(edge)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCumulativeWeight(self):
        return self.cumulative_weight

    def setCumulativeWeight(self, cumulative_weight):
        self.cumulative_weight = cumulative_weight


# This structure is not important because we never used it, we were supposed
# to keep just the frontier on memory and not the entire graph
class Graph:
    def __init__(self, name, start=None, goal=None):
        self.name = name
        self.start = start
        self.goal = goal
        self.vertexes = []

    def appendVertex(self, vertex):
        self.vertexes.append(vertex)

    def buildGraph(self, file_name):
        file_object = open(file_name, 'w')

        current_state = None
        v = None
        e = None

        for line in file_object:
            if(line.startswith('ini')):
                start = line.split('(')[1].split(')')[0]
                self.start = start
            elif(line.startswith('fin')):
                goal = line.split('(')[1].split(')')[0]
                self.goal = goal
            elif(line.startswith('cam')):
                path = line.split('(')[1].split(')')[0].split(',')
                state = path[0]
                next_state = path[1]
                weight = path[2]
                if(state != current_state):
                    v = Vertex(state)
                    e = Edge(next_state, weight)
                    v.appendEdge(e)
                    current_state = state
                elif(state == current_state):
                    e = Edge(next_state, weight)
                    v.appendEdge(e)
            elif(line.startswith('h')):
                heuristic = line.split('(')[1].split(')')[0].split(',')
                start = heuristic[0]
                goal = heuristic[1]
                h = heuristic[2]
            else:
                print(line)

        file_object.close()
