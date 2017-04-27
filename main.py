# Breadth First Search Implementation


class Edge():
    def __init__(self, origin, destiny, weight=1):
        self.origin = origin
        self.destiny = destiny
        self.weight = weight


class Vertex():
    def __init__(self, name, weight=1):
        self.name = name
        self.weight = weight
        self.edges = []


class Graph():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.vertexes = []
