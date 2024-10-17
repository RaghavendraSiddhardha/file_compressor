import os
from huffman_encode import huffman_encoding
from huffman_decode import huffman_decoding
from pathlib import Path

def get_file_path():
    """Prompt the user for a file path and validate it."""
    while True:
        file_path = input("Enter the path of the file (or type 'exit' to quit): ").strip().strip('"')
        if file_path.lower() == 'exit':
            return None
        if not file_path:
            print("File path cannot be empty.")
        elif not os.path.exists(file_path):
            print("File does not exist. Please enter a valid file path.")
        else:
            return file_path

def get_operation():
    """Prompt the user for the desired operation (compress or decompress)."""
    while True:
        operation = input("Type '1' to compress, '2' to decompress, or 'exit' to quit: ").strip()
        if operation.lower() == 'exit':
            return None
        if operation not in ("1", "2"):
            print("Invalid choice. Please enter '1' for compress or '2' for decompress.")
        else:
            return operation

def compress_file(file_path):
    """Compress the specified file and print the results."""
    try:
        compressed_file_path = huffman_encoding(file_path)
        print(f"File compressed and saved to {compressed_file_path}")

        original_size = Path(file_path).stat().st_size
        encoded_size = Path(compressed_file_path).stat().st_size
        memory_saved = (original_size - encoded_size) / 1024  # Convert to KB

        print(f"Original file size: {original_size} bytes")
        print(f"Encoded file size: {encoded_size} bytes")
        print(f"Memory saved: {memory_saved:.2f} KB")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

def decompress_file(file_path):
    """Decompress the specified file."""
    try:
        if not file_path.endswith(".compressed.hf"):
            print("The file does not appear to be a compressed Huffman file.")
            return

        decompressed_file_path = huffman_decoding(file_path)
        print(f"File decompressed and saved to {decompressed_file_path}")
    except Exception as e:
        print(f"An error occurred during decompression: {e}")

def main():
    print("Huffman Coding")
    while True:
        file_path = get_file_path()
        if file_path is None:
            print("Exiting the program. Goodbye!")
            break

        operation = get_operation()
        if operation is None:
            print("Exiting the program. Goodbye!")
            break

        if operation == "1":
            if input("Are you sure you want to compress this file? (y/n): ").lower() == 'y':
                compress_file(file_path)
            else:
                print("Compression cancelled.")
        elif operation == "2":
            if input("Are you sure you want to decompress this file? (y/n): ").lower() == 'y':
                decompress_file(file_path)
            else:
                print("Decompression cancelled.")

if __name__ == "__main__":
    main()
