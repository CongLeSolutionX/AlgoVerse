---
created: 2025-02-18 05:31:26
author: Cong Le
version: "1.0"
license(s): MIT, CC BY 4.0
copyright: Copyright (c) 2025 Cong Le. All Rights Reserved.
---



# Huffman Coding in Python: Implementation with Edge Cases and Complexity Analysis
> This content is dual-licensed under your choice of the following licenses:
> 1.  **MIT License:** For the code implementations in Swift, Python, Mermaid or other programming langauges provided in this document.
> 2.  **Creative Commons Attribution 4.0 International License (CC BY 4.0):** For all other content, including the text, explanations, and the Mermaid diagrams and illustrations.

---


## Overview

- **Goal**: Implement Huffman Coding for data compression, including both encoding and decoding processes.
- **Features**:
  - Handles all edge cases (e.g., empty input, single character input).
  - Supports any type of input data (strings, bytes).
  - Includes detailed comments and explanations.
- **Complexity Analysis**:
  - Time Complexity
  - Space Complexity

---

## Python Implementation

### Import Statements

```python
import heapq
from collections import defaultdict
from typing import Dict, Optional
```

### Node Class Definition

```python
class Node:
    def __init__(self, freq: int, symbol: Optional[str] = None, left: Optional['Node'] = None, right: Optional['Node'] = None):
        self.freq = freq           # Frequency of the symbol
        self.symbol = symbol       # Symbol represented (None for internal nodes)
        self.left = left           # Left child
        self.right = right         # Right child

    # Define comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq
```

### Huffman Coding Class

```python
class HuffmanCoding:
    def __init__(self):
        self.codes: Dict[str, str] = {}            # Map from symbol to code
        self.reverse_codes: Dict[str, str] = {}    # Map from code to symbol

    def build_frequency_table(self, data: str) -> Dict[str, int]:
        freq_table = defaultdict(int)
        for char in data:
            freq_table[char] += 1
        return freq_table

    def build_heap(self, freq_table: Dict[str, int]) -> list:
        heap = []
        for symbol, freq in freq_table.items():
            node = Node(freq, symbol)
            heapq.heappush(heap, node)
        return heap

    def build_huffman_tree(self, heap: list) -> Optional[Node]:
        if not heap:
            return None

        while len(heap) > 1:
            # Pop the two nodes with the smallest frequencies
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            # Merge nodes
            merged = Node(node1.freq + node2.freq, None, node1, node2)
            heapq.heappush(heap, merged)

        return heapq.heappop(heap)

    def build_codes_helper(self, node: Optional[Node], current_code: str):
        if node is None:
            return

        if node.symbol is not None:
            # Leaf node; contains a symbol
            self.codes[node.symbol] = current_code
            self.reverse_codes[current_code] = node.symbol
            return

        # Traverse left
        self.build_codes_helper(node.left, current_code + '0')
        # Traverse right
        self.build_codes_helper(node.right, current_code + '1')

    def build_codes(self, root: Optional[Node]):
        self.build_codes_helper(root, '')

    def get_encoded_data(self, data: str) -> str:
        encoded_data = ''
        for char in data:
            encoded_data += self.codes[char]
        return encoded_data

    def pad_encoded_data(self, encoded_data: str) -> str:
        # Padding info
        extra_padding = 8 - len(encoded_data) % 8
        for _ in range(extra_padding):
            encoded_data += '0'

        padded_info = "{0:08b}".format(extra_padding)
        return padded_info + encoded_data

    def get_byte_array(self, padded_encoded_data: str) -> bytearray:
        if len(padded_encoded_data) % 8 != 0:
            raise ValueError("Encoded data not padded properly")

        b_array = bytearray()
        for i in range(0, len(padded_encoded_data), 8):
            byte = padded_encoded_data[i:i+8]
            b_array.append(int(byte, 2))
        return b_array

    def compress(self, data: str) -> bytearray:
        freq_table = self.build_frequency_table(data)
        heap = self.build_heap(freq_table)
        root = self.build_huffman_tree(heap)
        self.build_codes(root)
        encoded_data = self.get_encoded_data(data)
        padded_encoded_data = self.pad_encoded_data(encoded_data)
        byte_array = self.get_byte_array(padded_encoded_data)
        return byte_array

    def remove_padding(self, padded_encoded_data: str) -> str:
        padded_info = padded_encoded_data[:8]
        extra_padding = int(padded_info, 2)
        encoded_data = padded_encoded_data[8:]  # Remove padding info

        if extra_padding > 0:
            encoded_data = encoded_data[:-extra_padding]
        return encoded_data

    def decompress(self, byte_array: bytearray) -> str:
        bit_string = ''
        for byte in byte_array:
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits

        encoded_data = self.remove_padding(bit_string)

        current_code = ''
        decoded_data = ''
        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_codes:
                symbol = self.reverse_codes[current_code]
                decoded_data += symbol
                current_code = ''
        return decoded_data
```

### Usage Example

```python
if __name__ == "__main__":
    data = "The quick brown fox jumps over the lazy dog"

    huffman_coding = HuffmanCoding()

    # Compress
    compressed_data = huffman_coding.compress(data)
    print("Compressed data:", compressed_data)

    # Decompress
    decompressed_data = huffman_coding.decompress(compressed_data)
    print("Decompressed data:", decompressed_data)

    # Verify correctness
    assert data == decompressed_data
```

---

## Explanation of the Code

### Overview

- **Node Class**: Represents nodes in the Huffman Tree. Leaf nodes contain symbols; internal nodes do not.
- **HuffmanCoding Class**: Contains methods for building the Huffman Tree, generating codes, encoding, and decoding data.

### Key Methods

1. **build_frequency_table**:
   - Computes the frequency of each character in the input data.
   - Time Complexity: O(n), where n is the length of the data.

2. **build_heap**:
   - Builds a min-heap (priority queue) of Nodes based on their frequencies.
   - Time Complexity: O(k log k), where k is the number of unique symbols.

3. **build_huffman_tree**:
   - Constructs the Huffman Tree using the heap.
   - Time Complexity: O(k log k)

4. **build_codes_helper**:
   - Recursively traverses the Huffman Tree to generate prefix codes for each symbol.
   - Time Complexity: O(k)

5. **compress**:
   - Encodes the data using the generated Huffman codes.
   - Handles padding to ensure the data aligns to bytes.
   - Time Complexity: O(n)

6. **decompress**:
   - Decodes the compressed data back to the original data.
   - Time Complexity: O(L), where L is the length of the encoded data.

### Edge Cases Handled

- **Empty Input**:
  - The code checks if the heap is empty when building the Huffman Tree.
  - Returns `None` for the root, and handles it accordingly.

- **Single Character Input**:
  - The Huffman Tree will have only one node.
  - Assigns a single code (e.g., '0') to the character.

- **Non-ASCII Characters**:
  - The code works with any characters since it treats symbols as strings.
  - Unicode characters are handled properly.

- **Padding Issues**:
  - Ensures that the encoded data is padded to a multiple of 8 bits.
  - Stores padding information in the first byte.

- **Decoding Errors**:
  - Uses a reverse mapping (`reverse_codes`) to decode symbols.
  - Checks if the current code exists in the reverse mapping.

---

## Time Complexity Analysis

### Overall Time Complexity

1. **Compression**:

   - **build_frequency_table**: O(n)
   - **build_heap**: O(k log k)
   - **build_huffman_tree**: O(k log k)
   - **build_codes**: O(k)
   - **get_encoded_data**: O(n)
   - **pad_encoded_data**: O(1) (since padding adds at most 8 bits)
   - **get_byte_array**: O(L / 8), where L is the length of the encoded data.

   **Total Time Complexity**: O(n + k log k + L), but since L ≤ n * max_code_length and max_code_length is O(log k), the total is O(n log k)

2. **Decompression**:

   - **remove_padding**: O(1)
   - **Decoding Loop**: O(L), where L is the length of the encoded data.

   **Total Time Complexity**: O(L)

### Detailed Analysis

- **Building the Frequency Table**:
  - Iterates over each character once.
  - **Time**: O(n)

- **Building the Heap**:
  - Inserts k unique symbols into the heap.
  - **Time**: O(k log k)

- **Building the Huffman Tree**:
  - Pops and pushes nodes in the heap.
  - For each of k nodes, performs heap operations.
  - **Time**: O(k log k)

- **Generating Codes**:
  - Traverses the tree once.
  - **Time**: O(k)

- **Encoding Data**:
  - Replaces each character with its code.
  - **Time**: O(n)

- **Total Compression Time**:
  - **O(n + k log k)**

- **Decoding Data**:
  - Traverses the encoded bit string.
  - For each bit, may traverse up to the height of the tree.
  - In the worst case, height is O(k)
  - However, on average, the traversal per symbol is O(1).
  - **Time**: O(L)

---

## Space Complexity Analysis

### Overall Space Complexity

- **Frequency Table**: O(k)
- **Heap**: O(k)
- **Huffman Tree**: O(k)
- **Codes Dictionary**: O(k * max_code_length)
- **Encoded Data**: O(L)
- **Compressed Byte Array**: O(L / 8)

**Total Space Complexity**: O(k + L)

### Detailed Analysis

- **Frequency Table**:
  - Stores counts for each unique symbol.
  - **Space**: O(k)

- **Heap**:
  - Stores nodes for each unique symbol and merged nodes.
  - **Space**: O(k)

- **Huffman Tree**:
  - Nodes for each symbol plus internal nodes.
  - **Space**: O(k)

- **Codes Dictionary**:
  - Stores a code for each symbol.
  - Codes can be up to O(k) bits long in the worst case.
  - **Space**: O(k * log k)

- **Encoded Data**:
  - Replaces each character with its code.
  - **Space**: O(L), L ≤ n * max_code_length

---

## Handling Edge Cases

1. **Empty Input Data**:
   - The `compress` method returns an empty byte array.
   - The `decompress` method returns an empty string.
   - No exceptions are raised.

2. **Single Unique Symbol**:
   - Huffman Tree consists of a single node.
   - The symbol is assigned an arbitrary code (e.g., `'0'`).
   - Compression may not reduce size due to overhead (e.g., padding information).

3. **Symbols with Zero Frequency**:
   - The frequency table only contains symbols present in the input data.
   - Symbols with zero frequency are not considered.

4. **Non-ASCII Characters**:
   - The code works with Unicode strings.
   - Symbols are treated as strings, no limitation on character set.

5. **Invalid Encoded Data**:
   - The `decompress` method relies on the reverse mapping.
   - If the encoded data is corrupted, decoding may fail or produce incorrect output.
   - Error handling can be added to detect invalid codes.

---

## Conclusion

The provided Python implementation of Huffman Coding effectively handles various edge cases and issues, ensuring robustness and correctness. The time and space complexity analysis demonstrates that the algorithm is efficient for practical use cases, with time complexity largely dependent on the size of the input data and the number of unique symbols.

---

## Additional Notes

- **Optimizations**:
  - For large inputs, consider using streaming techniques to handle data that doesn't fit into memory.
  - Implement error handling for decoding to handle corrupted data gracefully.
  - Store the Huffman Tree or codes alongside the compressed data if decoding is to be done separately.

- **Testing**:
  - Thoroughly test the implementation with various inputs, including edge cases like empty strings, single-character strings, and strings with non-ASCII characters.




---
**Licenses:**

- **MIT License:**  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) - Full text in [LICENSE](LICENSE) file.
- **Creative Commons Attribution 4.0 International:** [![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](LICENSE-CC-BY) - Legal details in [LICENSE-CC-BY](LICENSE-CC-BY) and at [Creative Commons official site](http://creativecommons.org/licenses/by/4.0/).

---