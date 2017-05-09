# Graph Structure and Parser


class Edge:
    def __init__(self, to, weight=1):
        self.to = to
        self.weight = weight


class Vertex:
    def __init__(self, name, h=1):
        self.name = name
        self.h = h
        self.edges = []
        self.visited = False

    def setVisited(self, value):
        self.visited = value

    def appendEdge(self, edge):
        self.edges.append(edge)

    def setH(self, h):
        self.h = h


class Graph:
    def __init__(self, name):
        self.name = name
        self.start = None
        self.goal = None
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