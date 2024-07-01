import heapq
from collections import defaultdict
from bitarray import bitarray
import os

class TreeNode:
    def __init__(self, val=(-1, 0)):
        self.val = val
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.val[1] < other.val[1]

def build_huffman_tree(freq):
    pq = [TreeNode((char, freq)) for char, freq in freq.items()]
    heapq.heapify(pq)
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = TreeNode((-1, left.val[1] + right.val[1]))
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)
    return heapq.heappop(pq)

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.left is None and node.right is None:
        codebook[node.val[0]] = prefix
    if node.left:
        generate_codes(node.left, prefix + '0', codebook)
    if node.right:
        generate_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(file_path):
    freq = defaultdict(int)
    binary_text = bitarray()
    output_file_path = file_path + ".compressed.hf"
    
    # Calculate frequency of each byte
    with open(file_path, 'rb') as file:
        while (byte := file.read(1)):
            freq[byte[0]] += 1
    
    # Build Huffman Tree
    huffman_tree = build_huffman_tree(freq)
    
    # Generate Huffman Codes
    huffman_codes = generate_codes(huffman_tree)
    
    # Serialize Huffman Codes
    marker = '{' + ','.join(f'{key}:{value}' for key, value in huffman_codes.items()) + '}'
    marker_bits = ''.join(f'{ord(c):08b}' for c in marker)
    
    # Convert text to binary using Huffman Codes
    with open(file_path, 'rb') as file:
        while (byte := file.read(1)):
            binary_text.extend(huffman_codes[byte[0]])
    
    # Add marker and padding
    binary_text = bitarray(marker_bits) + binary_text
    padding_length = 8 - (len(binary_text) % 8)
    if padding_length != 8:
        binary_text.extend('0' * padding_length)
    
    # Write binary data to output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(binary_text.tobytes())
        output_file.write(bytes([padding_length]))

    return output_file_path

