# BreadthFirstSearch implementation

import structure as graph


def BreadthFirstSearch(file_name):
    file_object = open(file_name, 'r')
    start = None
    goal = None
    frontier = []
    finished = False
    v = graph.Vertex()
    e = None
    complete_path = []

    print('Starting Breadth First Search')

    for line in file_object:
        if (line.startswith('ini')):
            start = line.split('(')[1].split(')')[0].strip()
            v.setName(start)
            frontier.append(v)
        elif (line.startswith('fin')):
            goal = line.split('(')[1].split(')')[0].strip()
            break

    print('Starting state:', start)
    print('Goal:', goal)

    if start == goal:
        finished = True

    while(frontier and not finished):

        file_object.seek(0, 0)
        for line in file_object:
            if (line.startswith('cam')):
                path = line.split('(')[1].split(')')[0].split(',')
                state = path[0].strip()
                next_state = path[1].strip()
                weight = path[2].strip()
                if(state == frontier[0].getName()):
                    e = graph.Edge(next_state, weight)
                    v.appendEdge(e)

        complete_path.append(frontier[0].getName())
        frontier.pop(0)

        if v.getEdges():
            edges = sorted(v.getEdges(), key=lambda edge: edge.weight)
            for edge in edges:
                v_aux = graph.Vertex(edge.getTo())
                frontier.append(v_aux)

        if frontier:
            v = frontier[0]

        if v.getName() == goal:
            finished = True

    file_object.close()
    print(complete_path)
    if not finished:
        print('Goal not found!')
    else:
        print('Goal reached:', v.getName())
