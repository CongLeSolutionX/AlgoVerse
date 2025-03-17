import heapq
import math
from typing import List, Tuple, Dict, Optional

class Node:
    """
    Represents a node in the graph.

    Attributes:
        x (int): X-coordinate of the node.
        y (int): Y-coordinate of the node.
        g (float): Cost from the start node to this node.
        h (float): Heuristic estimate from this node to the goal.
        f (float): Total cost (g + h).
        parent (Node): Parent node in the path.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.g = float('inf')  # Initialize with infinity
        self.h = 0.0
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        """
        Less-than comparison for priority queue sorting (based on f value).
        """
        return self.f < other.f
    
    def __eq__(self, other):
        """
        Equality comparison based on coordinates.  Essential for efficient
        membership testing in sets and dictionaries.
        """
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        """
        Hash function based on coordinates.  Essential for using Nodes
        as keys in sets and dictionaries.
        """
        return hash((self.x, self.y))


class BinaryHeapAStar:
    """
    A* algorithm implementation using a binary heap (heapq).
    """
    def __init__(self, grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int], heuristic_type: str = "manhattan"):
        """
        Initializes the A* solver.

        Args:
            grid: 2D list representing the graph (0 = walkable, 1 = obstacle).
            start: Tuple (x, y) for the starting node.
            goal: Tuple (x, y) for the goal node.
            heuristic_type:  Type of heuristic to use ('manhattan' or 'euclidean').
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.heuristic_type = heuristic_type
        self.open_set: List[Node] = []  # Use heapq for the open set (priority queue)
        self.closed_set: set[Node] = set() # Use a set for efficient membership testing
        self.nodes: Dict[Tuple[int, int], Node] = {} # Map coordinates to Node objects

        # Create Node objects for all grid positions.  This allows efficient
        # lookup and updates of node information during the search.
        for r in range(self.rows):
            for c in range(self.cols):
                self.nodes[(r, c)] = Node(r, c)

        self.start.g = 0
        self.start.h = self.heuristic(self.start)
        self.start.f = self.start.g + self.start.h
        heapq.heappush(self.open_set, self.start)  # Push the start node onto the heap



    def heuristic(self, node: Node) -> float:
        """
        Calculates the heuristic distance between a node and the goal.

        Args:
            node: The current node.

        Returns:
            The heuristic distance.
        """
        dx = abs(node.x - self.goal.x)
        dy = abs(node.y - self.goal.y)

        if self.heuristic_type == "manhattan":
            return dx + dy
        elif self.heuristic_type == "euclidean":
            return math.sqrt(dx * dx + dy * dy)
        else:
            raise ValueError("Invalid heuristic type")

    def get_neighbors(self, node: Node) -> List[Node]:
        """
        Gets the valid neighbor nodes of a given node.

        Args:
            node: The current node.

        Returns:
            A list of valid neighbor nodes.
        """
        neighbors: List[Node] = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4-directional movement
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0:
                neighbors.append(self.nodes[(nx, ny)])
        return neighbors

    def a_star_search(self) -> Optional[List[Tuple[int, int]]]:
        """
        Performs the A* search.

        Returns:
            A list of (x, y) tuples representing the path if found, otherwise None.
        """

        while self.open_set:
            current_node = heapq.heappop(self.open_set) # Get the node with the lowest f value

            if current_node == self.goal:
                return self.reconstruct_path(current_node)

            self.closed_set.add(current_node)

            for neighbor in self.get_neighbors(current_node):
                if neighbor in self.closed_set:
                    continue  # Skip nodes that have already been evaluated

                tentative_g = current_node.g + 1  # Cost to move to neighbor (assuming cost 1)

                if tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor)
                    neighbor.f = neighbor.g + neighbor.h

                    if neighbor not in self.open_set:
                        heapq.heappush(self.open_set, neighbor) # Add to open set if not already there
                    else:
                        # Node is already in the open set, so we need to "decrease-key"
                        # heapq doesn't directly support decrease-key, but we can achieve
                        # the same effect by re-pushing the node with the updated f value.
                        # This is valid because the node with the lower f will be popped first.
                        heapq.heapify(self.open_set) # Re-heapify to maintain heap property
        return None  # No path found


    def reconstruct_path(self, node: Node) -> List[Tuple[int, int]]:
        """
        Reconstructs the path from the goal node back to the start node.

        Args:
            node: The current node (goal node).

        Returns:
            A list of (x, y) tuples representing the path.
        """
        path = []
        while node:
            path.append((node.x, node.y))
            node = node.parent
        return path[::-1]  # Reverse the path to get it from start to goal



class FibonacciHeap:
    """
    A simplified Fibonacci Heap implementation (for demonstration purposes).
    This is NOT a full, robust Fibonacci Heap.  It only implements the
    necessary operations for A* (insert, extract-min, decrease-key).

    A real-world Fibonacci Heap implementation would be significantly more
    complex to handle cascading cuts, merging, etc., efficiently.
    """

    class Node:
        def __init__(self, data, key):
            self.data = data
            self.key = key
            self.degree = 0
            self.parent = None
            self.child = None
            self.left = None
            self.right = None
            self.mark = False

        def __lt__(self, other):
            return self.key < other.key

    def __init__(self):
        self.min_node = None
        self.num_nodes = 0
        self.node_map: Dict[any, FibonacciHeap.Node] = {}

    def is_empty(self):
        return self.min_node is None

    def insert(self, data, key):
        node = self.Node(data, key)
        node.left = node
        node.right = node
        self.node_map[data] = node
        self._add_to_root_list(node)
        self.num_nodes += 1
        return node  # Return the node to allow for decrease_key later

    def _add_to_root_list(self, node):
        if self.min_node is None:
            self.min_node = node
        else:
            node.right = self.min_node
            node.left = self.min_node.left
            self.min_node.left.right = node
            self.min_node.left = node
            if node.key < self.min_node.key:
                self.min_node = node

    def extract_min(self):
        if self.min_node is None:
            return None

        min_node = self.min_node
        # Add min_node's children to the root list
        if min_node.child is not None:
            child = min_node.child
            current = child
            while True:
                next_node = current.right
                self._add_to_root_list(current)
                current.parent = None  # Remove parent pointer
                current = next_node
                if current == child:
                    break

        # Remove min_node from root list
        self._remove_from_root_list(min_node)

        if min_node == min_node.right:
            self.min_node = None
        else:
            self.min_node = min_node.right
            self._consolidate()
        self.num_nodes -= 1

        del self.node_map[min_node.data] #Remove from the node_map
        return min_node.data

    def _remove_from_root_list(self, node):
        if node == self.min_node and node.right == node:  # Only node in the list
            self.min_node = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if node == self.min_node:  # If we removed the minimum node
                self.min_node = node.right

    def _consolidate(self):
        """
        Consolidates the heap after extract-min.  This is where the
        logarithmic amortized time for extract-min comes from.
        """
        degree_table = [None] * int(math.log2(self.num_nodes) * 2) # + 1

        # Create a list of root nodes to iterate through
        root_list = []
        current = self.min_node
        if current is not None:
            while True:
                root_list.append(current)
                current = current.right
                if current == self.min_node:
                    break
        
        # Iterate through root nodes and consolidate
        for node in root_list:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node  # Ensure 'node' has the smaller key

                self._link(other, node)  # Link 'other' as a child of 'node'
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        # Rebuild the root list and find the new minimum node
        self.min_node = None
        for i in range(len(degree_table)):
            if degree_table[i] is not None:
                self._add_to_root_list(degree_table[i])  # Add back to root list


    def _link(self, y, x):
        """
        Links node y as a child of node x.
        """
        self._remove_from_root_list(y)  # Remove y from the root list
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.right = x.child
            y.left = x.child.left
            x.child.left.right = y
            x.child.left = y
        x.degree += 1
        y.mark = False #clear the mark of y


    def decrease_key(self, node, new_key):
        """
        Decreases the key of a node.

        Args:
            node: The node to decrease the key of.
            new_key: The new key value (must be smaller than the current key).
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")

        node.key = new_key
        parent = node.parent

        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node


    def _cut(self, x, y):
        """
        Cuts node x from its parent y, adding x to the root list.
        """
          # Remove x from y's child list
        if x.right == x:  # x is the only child
            y.child = None
        else:
            x.left.right = x.right
            x.right.left = x.left
            if y.child == x: #update y.child if x was the child
                y.child = x.right
        y.degree -= 1

        self._add_to_root_list(x)
        x.parent = None
        x.mark = False


    def _cascading_cut(self, y):
        """
        Performs cascading cuts up the tree.
        """
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

   
    def get_key(self, data):
        """
        Gets node's key.

        Args:
            node: The node to decrease the key of.
        Returns:
            node.key: current node's key.
        Raises:
            KeyError: If node not found.
        """
        node = self.node_map.get(data)
        if node is None:
            raise KeyError("Node not found in Fibonacci Heap")
        return node.key



class FibonacciHeapAStar:
    """
    A* algorithm implementation using a Fibonacci heap.
    """

    def __init__(self, grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int], heuristic_type: str = "manhattan"):
        """
        Initializes the A* solver.

        Args:
            grid: 2D list representing the graph (0 = walkable, 1 = obstacle).
            start: Tuple (x, y) for the starting node.
            goal: Tuple (x, y) for the goal node.
            heuristic_type:  Type of heuristic to use ('manhattan' or 'euclidean').
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start_coords = start
        self.goal_coords = goal
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.heuristic_type = heuristic_type
        self.open_set = FibonacciHeap() # Use custom Fibonacci Heap
        self.closed_set: set[Node] = set()
        self.nodes: Dict[Tuple[int, int], Node] = {}  # Map coordinates to Node objects

        # Create Node objects as in the binary heap version
        for r in range(self.rows):
            for c in range(self.cols):
                self.nodes[(r, c)] = Node(r, c)

        self.start.g = 0
        self.start.h = self.heuristic(self.start)
        self.start.f = self.start.g + self.start.h
        self.open_set.insert(self.start, self.start.f)  # Insert the start node



    def heuristic(self, node: Node) -> float:
        """
        Calculates the heuristic distance (same as in BinaryHeapAStar).
        """
        dx = abs(node.x - self.goal.x)
        dy = abs(node.y - self.goal.y)

        if self.heuristic_type == "manhattan":
            return dx + dy
        elif self.heuristic_type == "euclidean":
            return math.sqrt(dx * dx + dy * dy)
        else:
            raise ValueError("Invalid heuristic type")

    def get_neighbors(self, node: Node) -> List[Node]:
        """
        Gets the valid neighbor nodes (same as in BinaryHeapAStar).
        """
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0:
                neighbors.append(self.nodes[(nx, ny)])
        return neighbors

    def a_star_search(self) -> Optional[List[Tuple[int, int]]]:
        """
        Performs the A* search using a Fibonacci heap.
        """
        while not self.open_set.is_empty():
            current_node = self.open_set.extract_min()

            if current_node == self.goal:
                return self.reconstruct_path(current_node)

            self.closed_set.add(current_node)

            for neighbor in self.get_neighbors(current_node):
                if neighbor in self.closed_set:
                    continue

                tentative_g = current_node.g + 1

                if tentative_g < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor)
                    neighbor.f = neighbor.g + neighbor.h

                    try:
                        existing_node = self.open_set.node_map[neighbor]
                        #if neighbor.f < existing_node.key:
                        if neighbor.f < self.open_set.get_key(neighbor):
                            self.open_set.decrease_key(existing_node, neighbor.f)
                    except KeyError:
                        self.open_set.insert(neighbor, neighbor.f)
        return None


    def reconstruct_path(self, node: Node) -> List[Tuple[int, int]]:
        """
        Reconstructs the path (same as in BinaryHeapAStar).
        """
        path = []
        while node:
            path.append((node.x, node.y))
            node = node.parent
        return path[::-1]

#### Example Usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
goal = (4, 4)

# Binary Heap A*
binary_heap_solver = BinaryHeapAStar(grid, start, goal, heuristic_type="manhattan")
path_binary = binary_heap_solver.a_star_search()
print("Binary Heap Path:", path_binary)

# Fibonacci Heap A*
fibonacci_heap_solver = FibonacciHeapAStar(grid, start, goal, heuristic_type="manhattan")
path_fibonacci = fibonacci_heap_solver.a_star_search()
print("Fibonacci Heap Path:", path_fibonacci)

# Example with Euclidean distance
binary_heap_solver_euclidean = BinaryHeapAStar(grid, start, goal, heuristic_type="euclidean")
path_binary_euclidean = binary_heap_solver_euclidean.a_star_search()
print("Binary Heap Path (Euclidean):", path_binary_euclidean)

fibonacci_heap_solver_euclidean = FibonacciHeapAStar(grid, start, goal, heuristic_type="euclidean")
path_fibonacci_euclidean = fibonacci_heap_solver_euclidean.a_star_search()
print("Fibonacci Heap Path (Euclidean):", path_fibonacci_euclidean)


# Example with an obstacle grid that has no path
grid_no_path = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],  # No path to the goal
]

binary_heap_solver_no_path = BinaryHeapAStar(grid_no_path, start, goal)
path_binary_no_path = binary_heap_solver_no_path.a_star_search()
print("Binary Heap Path (No Path):", path_binary_no_path)  # Output: None

fibonacci_heap_solver_no_path = FibonacciHeapAStar(grid_no_path, start, goal)
path_fibonacci_no_path = fibonacci_heap_solver_no_path.a_star_search()
print("Fibonacci Heap Path (No Path):", path_fibonacci_no_path)  # Output: None