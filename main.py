import structure as struct


def BreadthFirstSearch(file_name):
    file_object = open(file_name, 'w')
    start = None
    goal = None
    frontier = []

    for line in file_object:
        if (line.startswith('ini')):
            start = line.split('(')[1].split(')')[0].strip()
        elif (line.startswith('fin')):
            goal = line.split('(')[1].split(')')[0].strip()
        elif (line.startswith('cam')):
            path = line.split('(')[1].split(')')[0].split(',')
            state = path[0]
            next_state = path[1]
            weight = path[2]

    file_object.close()


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
