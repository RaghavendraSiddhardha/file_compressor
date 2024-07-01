# Huffman File Compressor 📚

This project provides an implementation of Huffman encoding and decoding in Python. It consists of separate modules for encoding and decoding, and a main script to interact with the user.

## Files 📁

- `huffman_encode.py`: Contains the Huffman encoding function.
- `huffman_decode.py`: Contains the Huffman decoding function.
- `main.py`: The main script to interact with the user for file compression and decompression.

## Requirements 📦


Make sure you have Python installed. You will also need the `bitarray` library, which can be installed via pip:

```sh 
pip install bitarray
```

## Usage 🚀
### Step 1: Prepare Your Files
Ensure you have all the necessary files in the same directory:

`huffman_encode.py`
`huffman_decode.py`
`main.py`
### Step 2: Run the Main Script
Execute the main.py script. This script will prompt you for the path of the file you want to compress or decompress.

```sh
python main.py
```
### Step 3: Follow the Prompts
Enter the path of the file: Type the path of the file you want to compress or decompress.
Choose an operation: Type 1 to compress the file or 2 to decompress a previously compressed file.

## How It Works 🔍
### Encoding
#### The encoding process involves:

Calculating the frequency of each byte in the file.
Building a Huffman tree based on the byte frequencies.
Generating Huffman codes from the tree.
Encoding the file data using the generated codes.
Saving the encoded data along with the Huffman codes to a new file.
Decoding

#### The decoding process involves:

Reading the encoded file.
Extracting the Huffman codes and the encoded data.
Reconstructing the original file data using the Huffman codes.