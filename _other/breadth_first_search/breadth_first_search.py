import queue;

def breadth_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    queue_nodes = queue.Queue(len(graph))
    visited = set()
