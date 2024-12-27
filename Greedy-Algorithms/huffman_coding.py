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