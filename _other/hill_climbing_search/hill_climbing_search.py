import queue;

def hill_climbing_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
