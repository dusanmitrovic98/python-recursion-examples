import queue;

def breadth_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    queue_nodes.put(start)
    found_dest = False
    while (not found_dest) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        # process(node)
        for dest in graph[node]:
