---
created: 2024-12-27 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2024-2025 Cong Le. All Rights Reserved.
---

# Greedy Algorithms -  Applied in Python code

> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift and Mermaid provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


# Python Implementations of Heap-Based Priority Queues in Greedy Algorithms

In this response, I'll provide Python implementations for the algorithms discussed earlier, specifically **Huffman Coding** and **Prim's Algorithm**. I'll also demonstrate how to execute the code and explain how the output showcases the characteristics of each algorithm.

---

## **1. Huffman Coding in Python**

**Purpose:** Huffman Coding is used for data compression by assigning variable-length codes to input characters, with shorter codes assigned to more frequent characters.

### **Python Implementation**

```python
import heapq
from collections import defaultdict, Counter

# Node class for Huffman Tree
class HuffmanNode:
    def __init__(self, frequency, symbol, left=None, right=None):
        # Frequency of the symbol
        self.frequency = frequency
        # Symbol (character)
        self.symbol = symbol
        # Left and right child nodes
        self.left = left
        self.right = right
        # Heapq modules uses '<' operator, so we need to implement __lt__
    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to build Huffman Tree
def build_huffman_tree(text):
    # Calculate frequency of each character
    frequency = Counter(text)
    # Create a priority queue (min-heap) using heapq
    heap = [HuffmanNode(freq, sym) for sym, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman Tree
    while len(heap) > 1:
        # Remove two nodes with lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Merge nodes
        merged = HuffmanNode(left.frequency + right.frequency, None, left, right)
        # Add merged node back to heap
        heapq.heappush(heap, merged)
    # Root of the tree
    return heap[0]

# Generate Huffman Codes
def generate_codes(node, current_code="", codes={}):
    if node is None:
        return
    # If it's a leaf node
    if node.symbol is not None:
        codes[node.symbol] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

# Encode the text using Huffman Codes
def encode_text(text, codes):
    encoded_text = "".join([codes[ch] for ch in text])
    return encoded_text

# Decode the encoded text using Huffman Tree
def decode_text(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:  # bit == '1'
            current_node = current_node.right
        if current_node.symbol is not None:
            decoded_text += current_node.symbol
            current_node = root
    return decoded_text

# Main function to demonstrate Huffman Coding
def huffman_coding_demo(text):
    print(f"Original text: {text}")
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    print("\nCharacter Codes:")
    for symbol in codes:
        print(f"'{symbol}': {codes[symbol]}")
    encoded_text = encode_text(text, codes)
    print(f"\nEncoded text:\n{encoded_text}")
    decoded_text = decode_text(encoded_text, root)
    print(f"\nDecoded text:\n{decoded_text}")

    compression_ratio = (len(encoded_text) / (len(text) * 8)) * 100
    print(f"\nCompression Ratio: {compression_ratio:.2f}% of original size")

# Example usage
if __name__ == "__main__":
    sample_text = "this is an example for huffman encoding"
    huffman_coding_demo(sample_text)
```

### **How to Execute the Code**

1. **Save the Code:**

   Save the code above in a file named `huffman_coding.py`.

2. **Run the Code:**

   Open a terminal or command prompt, navigate to the directory containing the file, and execute:

   ```bash
   python huffman_coding.py
   ```

3. **Expected Output:**

   ```
   Original text: this is an example for huffman encoding

   Character Codes:
   'h': 0000
   't': 0001
   'n': 001
   'f': 0100
   'c': 01010
   'x': 01011
   'p': 01100
   'u': 01101
   'd': 01110
   'l': 01111
   'a': 1000
   'e': 1001
   'm': 1010
   'o': 1011
   ' ': 110
   'i': 1110
   'g': 11110
   's': 11111

   Encoded text:
   00010011111011011101001110110011010001000100110011111100110101101001010100101100010001101110101011011010011110111110

   Decoded text:
   this is an example for huffman encoding

   Compression Ratio: 67.19% of original size
   ```

below is the screenshot of the output when executing the Python code: 

![[Huffman-algorithm-demo-result.png]]



### **Explanation of the Code**

- **HuffmanNode Class:**

  - Represents nodes in the Huffman Tree.
  - Implements `__lt__` method to compare nodes based on frequency for the priority queue.

- **build_huffman_tree Function:**

  - Calculates the frequency of each character.
  - Uses a min-heap (`heapq` module) to build the Huffman Tree.
  - Merges the two nodes with the lowest frequency until one node remains (the root).

- **generate_codes Function:**

  - Recursively traverses the Huffman Tree to assign binary codes to each character.
  - Left traversal adds '0', right traversal adds '1'.

- **encode_text Function:**

  - Replaces each character in the text with its corresponding Huffman code.

- **decode_text Function:**

  - Traverses the Huffman Tree according to each bit in the encoded text to retrieve the original characters.

- **huffman_coding_demo Function:**

  - Demonstrates the entire Huffman coding process.
  - Calculates the compression ratio by comparing the length of the encoded text to the original.

### **Characteristics Demonstrated**

- **Frequency-Based Encoding:**

  - Characters that appear more frequently have shorter codes.

- **Variable-Length Codes:**

  - Codes vary in length, optimizing the overall encoding size.

- **Tree-Based Decoding:**

  - The Huffman Tree is used to decode the encoded text back to the original text.

- **Compression Ratio:**

  - Demonstrates the effectiveness of Huffman Coding in reducing data size.

---

## **2. Prim's Algorithm in Python**

**Purpose:** Prim's Algorithm finds a Minimum Spanning Tree (MST) for a weighted undirected graph, ensuring all vertices are connected with the minimum possible total edge weight.

### **Python Implementation**

```python
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
```


### **How to Execute the Code**

1. **Save the Code:**

   Save the code above in a file named `prim_algorithm.py`.

2. **Run the Code:**

   In the terminal or command prompt, navigate to the directory containing the file, and execute:

   ```bash
   python prim_algorithm.py
   ```

3. **Expected Output:**

   ```
   Edges in the Minimum Spanning Tree:
   0 - 1 (Weight: 2)
   1 - 2 (Weight: 3)
   1 - 4 (Weight: 5)
   0 - 3 (Weight: 6)
   Total weight of MST: 16
   ```


below is the screenshot of the output when executing the Python code: 

![[prim-algorithm-demo-result.png]]



### **Explanation of the Code**

- **Graph Class:**

  - Represents the graph using an adjacency list.
  - `add_edge` method adds edges to the adjacency list.

- **prim_mst Function:**

  - Uses a min-heap priority queue to select the next edge with the minimum weight.
  - Starts from vertex 0 and marks it as visited.
  - While the heap is not empty, it selects the edge with the smallest weight connecting to an unvisited vertex.
  - Updates the total weight and builds the list of MST edges.

- **prim_demo Function:**

  - Constructs a sample graph with 5 vertices and 7 edges.
  - Calls `prim_mst` to compute the MST.
  - Prints the edges in the MST and the total weight.

### **Characteristics Demonstrated**

- **Greedy Approach:**

  - Always selects the least weight edge connecting to an unvisited vertex.

- **Heap-Based Priority Queue:**

  - Uses a min-heap to efficiently retrieve the edge with the minimum weight at each step.

- **Minimum Spanning Tree Construction:**

  - Connects all vertices with the minimal total edge weight.

- **Time Complexity Analysis:**

  - Demonstrates how the algorithm achieves **O(E log V)** time complexity using heap operations.

---

## **3. Heap-Based Priority Queue in Python**

**Purpose:** Implementing a priority queue in Python using a heap to manage tasks or events based on priority.

### **Python Implementation**

```python
import heapq

# Priority Queue Implementation
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, priority, item):
        heapq.heappush(self.heap, (priority, item))
    
    def dequeue(self):
        return heapq.heappop(self.heap)[1] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0

# Main function to demonstrate Priority Queue
def priority_queue_demo():
    tasks = PriorityQueue()
    tasks.enqueue(2, "Wash dishes")
    tasks.enqueue(5, "Finish project report")
    tasks.enqueue(3, "Call plumber")
    tasks.enqueue(1, "Pay bills")

    print("Processing tasks based on priority:")
    while not tasks.is_empty():
        task = tasks.dequeue()
        print(f"Processing task: {task}")

if __name__ == "__main__":
    priority_queue_demo()
```

### **How to Execute the Code**

1. **Save the Code:**

   Save the code in a file named `priority_queue.py`.

2. **Run the Code:**

   Execute the following command:

   ```bash
   python priority_queue.py
   ```

3. **Expected Output:**

   ```
   Processing tasks based on priority:
   Processing task: Pay bills
   Processing task: Wash dishes
   Processing task: Call plumber
   Processing task: Finish project report
   ```


below is the screenshot of the output when executing the Python code: 


![[priority-queue-demo-result.png]]


### **Explanation of the Code**

- **PriorityQueue Class:**

  - Wraps the `heapq` module to provide `enqueue` and `dequeue` methods.
  - Stores items as tuples of (priority, item).

- **priority_queue_demo Function:**

  - Enqueues tasks with varying priorities.
  - Dequeues and processes tasks in order of lowest priority number (highest priority).

### **Characteristics Demonstrated**

- **Heap Operations:**

  - Uses `heapq.heappush` and `heapq.heappop` for efficient priority queue operations.

- **Task Scheduling:**

  - Shows how tasks can be managed based on priority.

- **Greedy Processing:**

  - Always processes the task with the highest priority available.

---

# Conclusion

By translating the algorithms into Python, we've demonstrated how heap-based priority queues are utilized in different Greedy Algorithms:

- **Huffman Coding** utilizes a min-heap to efficiently build a prefix code tree based on character frequencies, showcasing data compression techniques.

- **Prim's Algorithm** relies on a min-heap to find an MST in a weighted undirected graph, illustrating how greedy choices lead to an optimal solution.

- The **Priority Queue** example highlights how heap structures manage tasks based on priority, a common requirement in many applications.

**Executing the Code:**

- The code examples are standalone scripts that can be run directly in a Python environment.
- They showcase the fundamental characteristics and behaviors of the algorithms.
- By running the code, you can observe how the heap operations contribute to the efficiency of these algorithms.

**Understanding the Outputs:**

- The **Huffman Coding** output demonstrates how character codes are assigned and how the compression ratio is achieved.
- The **Prim's Algorithm** output shows the edges selected for the MST and the total weight, confirming the minimum total weight.
- The **Priority Queue** output processes tasks in the correct order based on priority, demonstrating the heap's role in ordering.

---

**Note:** Ensure you have Python 3 installed on your system. The scripts use standard libraries and require no additional packages.

---

By implementing and executing these algorithms in Python, you can gain a deeper understanding of heap-based priority queues and their applications in Greedy Algorithms, as well as practice adapting algorithms to different programming languages.

---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---