# In Graph theory, the depth-first search algorithm is mainly used to:

# Traverse all vertices in a “graph”;
# Traverse all paths between any two vertices in a “graph”.

# DFS: IJ TRICK: USE DS(STACK); Time Complexity: O(V + E).Space Complexity: O(V) (stack(manually created or from recursion) stores V vertices)


# defaultdict
from collections import defaultdict

# Generate adjacency list for undirected graph


def generateAdjacencyLst(edges):
    # it will be an empty list if for any key there exists no value
    adjacencyList = defaultdict(list)
    for u, v in edges:
        # print(u, v)
        # print(adjacencyList)
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList


edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], [
    'D', 'H'], ['D', 'I'], ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]
adjacencyList = generateAdjacencyLst(edges)
print(adjacencyList)

# defaultdict(<class 'list'>,
# {'A': ['B', 'C'],
# 'B': ['A', 'D', 'E'],
#  'C': ['A', 'F', 'G'],
#  'D': ['B', 'H', 'I'],
# 'E': ['B', 'J', 'K'],
# 'F': ['C', 'L', 'M'],
# 'G': ['C'],
#  'H': ['D'],
#  'I': ['D'],
#   'J': ['E'],
#   'K': ['E'],
#    'L': ['F'],
#    'M': ['F']}
#    )

# find dfs traversal from starting vertex


def dfs(adjacencyList, vertex, visitedSet=None, path=None):
    # create memo once in top-level call
    if visitedSet is None:
        visitedSet = set()
    if path is None:
        path = []

    visitedSet.add(vertex)
    path.append(vertex)
    print(visitedSet, "PATH", path)
    if vertex in adjacencyList:
        print("IN", vertex, adjacencyList[vertex])
        for neighbor in adjacencyList[vertex]:
            if neighbor not in visitedSet:
                print("calling dfs for", neighbor)
                dfs(adjacencyList, neighbor, visitedSet, path)
    return path


print(dfs(adjacencyList, 'A'))
