import queue;

def depth_first_search(graph, start, end):
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
        for dest in reversed(graph[node]):
            if dest not in visited:
