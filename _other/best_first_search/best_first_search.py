import queue;

def best_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    priority_queue = queue.PriorityQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    priority_queue.put((graph[start][0], start))
    found_dest = False
    while (not found_dest) and (not priority_queue.empty()):
        node = priority_queue.get()
        # process(node[1])
