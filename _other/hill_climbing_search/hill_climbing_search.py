import queue;

def hill_climbing_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    stack_nodes = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False
    while (not found_dest) and (not stack_nodes.empty()):
        node = stack_nodes.get()
        # process(node)
        destinations = list()
        for dest in graph[node][1]:
            element = (graph[dest][0], dest)
            destinations.append(element)
        for dest_heur in sorted(destinations, reverse=True):
            if dest_heur[1] not in visited:
                prev_nodes[dest_heur[1]] = node
                if dest_heur[1] is end:
