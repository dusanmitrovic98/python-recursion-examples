import queue;

def best_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    priority_queue = queue.PriorityQueue(len(graph))
    visited = set()
