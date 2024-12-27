import heapq

# Edge class (for clarity, not strictly necessary)
class Edge:
    def __init__(self, weight, src, dest):
        self.weight = weight
        self.src = src
        self.dest = dest

# Graph class using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjacency = [[] for _ in range(vertices)]
    
    def add_edge(self, src, dest, weight):
        self.adjacency[src].append((weight, dest))
        self.adjacency[dest].append((weight, src))  # Because undirected graph

def prim_mst(graph):
    V = graph.V
    visited = [False] * V
    min_heap = []
    mst_edges = []
    total_weight = 0

    # Start from vertex 0
    visited[0] = True
    for edge in graph.adjacency[0]:
        heapq.heappush(min_heap, (edge[0], 0, edge[1]))  # (weight, src, dest)

    while min_heap:
        weight, src, dest = heapq.heappop(min_heap)
        if not visited[dest]:
            visited[dest] = True
            mst_edges.append((src, dest, weight))
            total_weight += weight

            for edge in graph.adjacency[dest]:
                if not visited[edge[1]]:
                    heapq.heappush(min_heap, (edge[0], dest, edge[1]))
    
    return mst_edges, total_weight

# Main function to demonstrate Prim's Algorithm
def prim_demo():
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst_edges, total_weight = prim_mst(g)

    print("Edges in the Minimum Spanning Tree:")
    for edge in mst_edges:
        print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")
    print(f"Total weight of MST: {total_weight}")

if __name__ == "__main__":
    prim_demo()