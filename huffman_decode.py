from bitarray import bitarray

def huffman_decoding(file_path):
    # Read the encoded file
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # The last byte contains the padding length
    padding_length = file_data[-1]
    
    # Convert file data (excluding the last byte) to a bitarray
    binary_data = bitarray()
    binary_data.frombytes(file_data[:-1])
    
    # Remove the padding bits
    if padding_length != 8:
        binary_data = binary_data[:-padding_length]
    
    # Extract the marker and the encoded text
    marker_end_index = binary_data.search(bitarray('01111101'))[0] + 8  # '01111101' is the binary for '}'
    marker_bits = binary_data[:marker_end_index]
    encoded_text = binary_data[marker_end_index:]
    
    # Convert marker bits to string
    marker = ''.join(chr(int(marker_bits[i:i+8].to01(), 2)) for i in range(0, len(marker_bits), 8))
    
    # Parse the Huffman codes from the marker
    if marker[0] != '{' or marker[-1] != '}':
        raise ValueError("Invalid marker format")
    marker_content = marker[1:-1]  # Remove '{' and '}'
    huffman_codes = {}
    for item in marker_content.split(','):
        if ':' in item:
            key, value = item.split(':')
            huffman_codes[value] = int(key)
    
    # Decode the encoded text using Huffman codes
    decoded_bytes = bytearray()
    current_bits = ""
    for bit in encoded_text:
        current_bits += '1' if bit else '0'
        if current_bits in huffman_codes:
            decoded_bytes.append(huffman_codes[current_bits])
            current_bits = ""
    
    # Write the decoded bytes to a file
    output_file_path = file_path.replace(".compressed.hf", "")
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decoded_bytes)
    
    return output_file_path

