edges = [l.split(": ") for l in open("25.txt").read().splitlines()]
edges = set((v1, v2) for v1, vvv in edges for v2 in vvv.split(" "))
nodes = set(v for e in edges for v in e)
node_indices = { v: i for i, v in enumerate(nodes)}
adjacency_matrix = [[
    int((v1, v2) in edges or (v2, v1) in edges) for v1 in nodes
] for v2 in nodes]
print(adjacency_matrix)

# Karger's algorithm to find Minimum Cut in an
# undirected, unweighted and connected graph.
import random

# a class to represent a unweighted edge in graph
class Edge:
    def __init__(self, s, d):
        self.src = s
        self.dest = d

# a class to represent a connected, undirected
# and unweighted graph as a collection of edges.
class Graph:
    # V-> Number of vertices, E-> Number of edges
    def __init__(self, v, e):
        self.V = v
        self.E = e
        # graph is represented as an array of edges.
        # Since the graph is undirected, the edge
        # from src to dest is also edge from dest
        # to src. Both are counted as 1 edge here.
        self.edge = []

# A class to represent a subset for union-find
class subset:
    def __init__(self, p, r):
        self.parent = p
        self.rank = r

# A very basic implementation of Karger's randomized
# algorithm for finding the minimum cut. Please note
# that Karger's algorithm is a Monte Carlo Randomized algo
# and the cut returned by the algorithm may not be
# minimum always
def kargerMinCut(graph):
    # Get data of given graph
    V = graph.V
    E = graph.E
    edge = graph.edge
    # Allocate memory for creating V subsets.
    subsets = []
    # Create V subsets with single elements
    for v in range(V):
        subsets.append(subset(v, 0))
    # Initially there are V vertices in
    # contracted graph
    vertices = V
    # Keep contracting vertices until there are
    # 2 vertices.
    while vertices > 2:
        # Pick a random edge
        i = int(E * random.random())
        # Find vertices (or sets) of two corners
        # of current edge
        subset1 = find(subsets, edge[i].src)
        subset2 = find(subsets, edge[i].dest)
        # If two corners belong to same subset,
        # then no point considering this edge
        if subset1 == subset2:
            continue
        # Else contract the edge (or combine the
        # corners of edge into one vertex)
        else:
            # print("Contracting edge " + str(edge[i].src) + "-" + str(edge[i].dest))
            vertices -= 1
            Union(subsets, subset1, subset2)

    # Now we have two vertices (or subsets) left in
    # the contracted graph, so count the edges between
    # two components and return the count.
    cutedges = 0
    for i in range(E):
        subset1 = find(subsets, edge[i].src)
        subset2 = find(subsets, edge[i].dest)
        if subset1 != subset2:
            cutedges += 1

    return cutedges, subsets

# A utility function to find set of an element i
# (uses path compression technique)
def find(subsets, i):
    # find root and make root as parent of i
    # (path compression)
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)
    return subsets[i].parent

# A function that does union of two sets of x and y
# (uses union by rank)
def Union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    # Attach smaller rank tree under root of high
    # rank tree (Union by Rank)
    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot

    # If ranks are same, then make one as root and
    # increment its rank by one
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1

# Driver program to test above functions
def main():
    V = len(nodes)
    E = len(edges)
    graph = Graph(V, E)
    
    for v1, v2 in edges:
        graph.edge.append(Edge(node_indices[v1], node_indices[v2]))
    
    while True:
        cutedges, subsets = kargerMinCut(graph)
        print("Cut found by Karger's randomized algo is", cutedges)
        sizes = {}
        for i in range(V):
            sizes[find(subsets, i)] = sizes.get(find(subsets, i), 0)+1
        import math
        print(sizes)
        print(math.prod(sizes.values()))
        if cutedges == 3:
            exit()

if __name__ == '__main__':
    main()