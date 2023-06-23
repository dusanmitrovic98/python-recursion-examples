# A simple platform game is organized as a network of underground tunnels that intersect. 
# At each intersection, there are guardian robots that need to be overcome in order to 
# continue moving forward. Each tunnel is of the same length, and it takes the same 
# amount of time to overcome each guardian. At the beginning of the game, two players 
# are located at different intersections and want to join forces to overcome the guardians 
# more easily. Both players move at the same speed through the tunnels. Write a function named 
# 'join(map, intersection1, intersection2)' in the Python programming language that uses a 
# search algorithm to determine, based on the initial intersections of both players 
# (intersection1 and intersection2), the minimum number of guardians they need to overcome
# in order to join at one of the intersections in the game defined by the graph map." 
# Loops are forbidden! Only recursion! 

def join(map, intersection1, intersection2, visited=None):
    if visited is None:
        visited = set()  # Initialize the set of visited intersections

    # Base case: If the players are already at the same intersection, no guardians need to be overcome
    if intersection1 == intersection2:
        return 0

    # Recursive case: Find the neighbors of the current intersection and explore them recursively
    neighbors = map[intersection1]
    min_guards = float('inf')  # Initialize with a large value

    def traverse_neighbors(start, end, min_guards_param):
        if start <= end:
            if neighbors[start] not in visited:
                visited.add(neighbors[start])  # Add the current intersection to the visited set
                num_guards = join(map, neighbors[start], intersection2, visited)  # Recursive call
                visited.remove(neighbors[start])  # Remove the current intersection from the visited set
                min_guards_param = min_guards_param if (min_guards_param < num_guards) else num_guards
            min_guards_param = traverse_neighbors(start + 1, end, min_guards_param)
        return min_guards_param
    min_guards = traverse_neighbors(0, len(neighbors) - 1, min_guards)

    return min_guards + 1  # Add 1 for the current intersection guardian

# Example usage:
game_map = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

start1 = 'A'
start2 = 'D'
