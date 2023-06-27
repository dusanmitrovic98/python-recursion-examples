import queue;

def depth_first_search(graph, start, end):
    if start is end:
        path = list()
