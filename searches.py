import structure as graph


# Beginning of the BreadthFirstSearch algorithm
def BreadthFirstSearch(file_name):
    file_object = open(file_name, 'r')
    start = None
    goal = None
    frontier = []
    finished = False
    all_visited = False
    v = graph.Vertex()
    e = None
    complete_path = []

    print('Starting Breadth First Search')

    # This for loop will search the file to find the starting state
    # and the final state,
    # when it finds the starting state, it will set the neme of the vertex
    # created above with the starting state name and
    # then it will be added to the frontier list and setted as visited,
    # and the goal variable assigned above will store the final state's name.
    for line in file_object:
        if (start is not None and goal is not None):
            break
        if (line.startswith('ini')):
            start = line.split('(')[1].split(')')[0].strip()
            v.setName(start)
            v.setVisited(True)
            frontier.append(v)
        elif (line.startswith('fin')):
            goal = line.split('(')[1].split(')')[0].strip()

    print('Starting state:', start)
    print('Goal:', goal)

    # This line will verify if the starting state is already the desired one,
    # if so then the program will end.
    if start == goal:
        finished = True

    # This while loop will run until we find the desired state
    # or all nodes on the frontier list were all visited
    while(not all_visited and not finished):

        # This command will set the file's current position to the beginning
        # of the file
        file_object.seek(0)
        # This for loop will read all the lines of the file searching
        # which ones contains the vertices of the state stored on the
        # variable 'v', then it will create the objects edges with the relevant
        # information and then will add the edges on a list inside the vertex
        # 'v'
        for line in file_object:
            if (line.startswith('cam')):
                path = line.split('(')[1].split(')')[0].split(',')
                state = path[0].strip()
                if(state == v.getName()):
                    next_state = path[1].strip()
                    weight = path[2].strip()
                    e = graph.Edge(next_state, int(weight))
                    v.appendEdge(e)

        # If there is any edge on the vertex 'v' we will get that edges
        # and will sort using as reference the weight of the edge and
        # add them to a empty list, after that we will
        # create a vertex with each edge's name on the list. The vertexes
        # are added to the frontier list, but before we will check if there is
        # already a vertex with the same name on the frontier list, if not then
        # the vertex will be added to the frontier list.
        if v.getEdges():
            edges = sorted(v.getEdges(), key=lambda edge: edge.weight)
            for edge in edges:
                ed_exist = False
                for f in range(len(frontier)):
                    if(edge.getTo() == frontier[f].getName()):
                        ed_exist = True
                if(not ed_exist):
                    v_aux = graph.Vertex(edge.getTo())
                    frontier.append(v_aux)

        # If there is any vertex on the frontier list then we will assign
        # the vertex variable "v" with the first one on the list.
        # The variable 'c' is used to control if all states on the frontier
        # list were visited or not. The for loop will search for the first
        # non visited state on the list, then the variable 'v' will be assigned
        # with it, this state on the list will be market as visited and at last
        # we will add the name of this state in our complete_path variable.i
        # Each time we dont find a non visited state we will incremente c by 1.
        c = 1
        for f in range(len(frontier)):
            if (not frontier[f].getVisited()):
                v = frontier[f]
                frontier[f].setVisited(True)
                complete_path.append(v.getName())
                break
            c += 1
        # if 'c' is higher than the number of states on our frontier list then
        # we will know that all states were visited
        if c > len(frontier):
            all_visited = True
        # if not any(not vertex.visited for vertex in frontier):
            # all_visited = True

        # If the current vertex on the "v" variable contains the same name
        # as the desired state so we have reached our goal and our "finished"
        # variable will receive a "True" value
        if v.getName() == goal:
            finished = True

    # Here we gonna close the file, print our path and show a message
    # saying if we found our goal or not.
    file_object.close()
    print(complete_path)
    if not finished:
        print('Goal not found!')
        print('(,╯︵╰,)')
    else:
        print('Goal reached:', v.getName())
        print("\(◦'⌣'◦)/")


# Beginning of the A star algorithm
def A_star(file_name):
    file_object = open(file_name, 'r')
    start = None
    goal = None
    frontier = []
    finished = False
    v = graph.Vertex()
    e = None
    complete_path = []

    print('Starting A* Search')

    # This for loop will search the file to find the starting state
    # and the final state,
    # when it finds the starting state, it will set the neme of the vertex
    # created above with the starting state name a vertex with and
    # then it will be added to the frontier list,
    # and the goal variable assigned above will store the final state.
    for line in file_object:
        if (start is not None and goal is not None):
            break
        if (line.startswith('ini')):
            start = line.split('(')[1].split(')')[0].strip()
            v.setName(start)
            v.setVisited(True)
            frontier.append(v)
        elif (line.startswith('fin')):
            goal = line.split('(')[1].split(')')[0].strip()

    print('Starting state:', start)
    print('Goal:', goal)

    # This line will verify if the starting state is already the desired one,
    # if so then the program will end.
    if start == goal:
        finished = True

    # This while loop will run until we find the desired state
    # or the nodes on the frontier list are all gone
    while(frontier and not finished):

        # This command will set the file's current position to the beginning
        # of the file
        file_object.seek(0)
        # This for loop will read all the lines of the file searching
        # which ones contains the vertices of the first state on the frontier
        # list, then it will create the object edge with the relevant
        # information and then will add the edges on a list inside the vertex
        # that has the name of the first state on the frontier list
        # created on the beginning of the algorithm
        for line in file_object:
            if (line.startswith('cam')):
                path = line.split('(')[1].split(')')[0].split(',')
                state = path[0].strip()
                if(state == frontier[0].getName()):
                    next_state = path[1].strip()
                    weight = path[2].strip()
                    e = graph.Edge(next_state, int(weight))
                    v.appendEdge(e)

        # We will pop the first state on the frontier list
        frontier.pop(0)

        # If there is any edge on the vertex 'v' we will get that edges
        # and will sort using as reference the weight of the edge
        # and add them to a empty list
        if v.getEdges():
            edges = sorted(v.getEdges(), key=lambda edge: edge.weight)
            # after that we will create a vertex with each edge's
            # name on the edges' list.
            for edge in edges:
                v_aux = graph.Vertex(edge.getTo())
                # Before we add v_aux to our frontier list we need to
                # get back to the beginning of the file and start looking
                # for the heuristic of the state stored in the variable v_aux
                file_object.seek(0)
                for line in file_object:
                    if (line.startswith('h')):
                        heuristic = line.split('(')[1].split(')')[0].split(',')
                        origin = heuristic[0].strip()
                        goal = heuristic[1].strip()
                        h = heuristic[2].strip()
                        if v_aux.getName() == origin:
                            v_aux.setH(int(h))
                            break
                # after finding the heuristic we gonna sum the accumulated
                # weight stored on our variable "v" with the edge weight,
                # v_aux will receive this value
                v_aux.setCumulativeWeight(edge.getWeight()
                                          + v.getCumulativeWeight())
                # The vertexes are added to the frontier list.
                frontier.append(v_aux)

            # Now we sort our frontier list using as reference the cumulative
            # weight plus the heuristic of the states, so our algorithm
            # will always visit most promising state
            frontier = sorted(frontier,
                              key=lambda v: v.getCumulativeWeight() + v.getH())

        # If there is any vertex on the frontier list then we will assign
        # the vertex variable "v" with the first one on the list.
        if frontier:
            v = frontier[0]

        # The first name of the state on the frontier list will be added
        # to the complete_path list
        complete_path.append(frontier[0].getName())

        # If the current vertex on the "v" variable contains the same name
        # as the desired state so we have reached our goal and our "finished"
        # variable will receive a "True" value
        if v.getName() == goal:
            finished = True

    # Here we gonna close the file, print our path and show a message
    # saying if we found our goal or not.
    file_object.close()
    print(complete_path)
    if not finished:
        print('Goal not found!')
        print('(,╯︵╰,)')
    else:
        print('Goal reached:', v.getName())
        print("\(◦'⌣'◦)/")
