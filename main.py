import os
from huffman_encode import huffman_encoding
from huffman_decode import huffman_decoding
from pathlib import Path

def main():
    print("Huffman Coding")
    while True:
        file_path = input("Enter the path of the file: ").strip('""')
        if not file_path:
            print("File path cannot be empty.")
            continue
        if not os.path.exists(file_path):
            print("File does not exist. Please enter a valid file path.")
            continue
        break
    
    while True:
        operation = input("type 1 to compress or type 2 to de-compress: ")
        if operation not in ("1", "2"):
            print("Invalid choice. Please enter 'compress' or 'decompress'.")
            continue
        break
    
    if operation == "1":
        compressed_file_path = huffman_encoding(file_path)
        print(f"File compressed and saved to {compressed_file_path}")
        original_size=Path(file_path).stat().st_size
        encoded_size=Path(file_path+".compressed.hf").stat().st_size
        memory_saved=float(original_size-encoded_size)/1024
        print(f"Original file size: {original_size} bytes")
        print(f"Encoded file size: {encoded_size} bytes")
        print(f"memory saved: {memory_saved} kilo-bytes")
    elif operation == "2":
        if not file_path.endswith(".compressed.hf"):
            print("The file does not appear to be a compressed Huffman file.")
        else:
            decompressed_file_path = huffman_decoding(file_path)
            print(f"File decompressed and saved to {decompressed_file_path}")

if __name__ == "__main__":
    main()
