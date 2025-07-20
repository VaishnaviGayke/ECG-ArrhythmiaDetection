import sys


def remove_duplicates(keyword):
    seen = set()
    new_keyword = ""
    for char in keyword:
        if char == 'j':  # Treat 'i' and 'j' as the same
            char = 'i'
        if char not in seen:
            new_keyword += char
            seen.add(char)
    print(f"Removing duplicates from keyword: {new_keyword}")
    return new_keyword


def generate_playfair_matrix(keyword):
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # 'i' and 'j' are treated as the same
    matrix = []
    used_chars = set(keyword)

    # Add keyword letters to the matrix
    for char in keyword:
        if char not in matrix:
            matrix.append(char)

    # Add the rest of the alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    # Convert list to a 5x5 matrix
    playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    print("The playfair matrix is:")
    for row in playfair_matrix:
        print(" ".join(row))
    return playfair_matrix


def preprocess_text(text):
    text = text.replace('j', 'i')  # Replace 'j' with 'i'
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result += 'x'
        elif i + 1 < len(text):
            result += text[i + 1]
        i += 2
    if len(result) % 2 == 1:
        result += 'x'
    return result


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def encrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        # Same row: Shift right
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column: Shift down
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        # Rectangle: Swap columns
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_pair(matrix, pair):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:
        # Same row: Shift left
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column: Shift up
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        # Rectangle: Swap columns
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_cipher(keyword, text, mode):
    keyword = remove_duplicates(keyword)
    matrix = generate_playfair_matrix(keyword)

    if mode == 'enc':
        print("Please enter the plaintext:")
        text = preprocess_text(text)
        print(f"Plaintext with fillers: {text}")
        result = ""
        for i in range(0, len(text), 2):
            result += encrypt_pair(matrix, text[i:i + 2])
        return result

    elif mode == 'dec':
        print("Please enter the ciphertext:")
        result = ""
        for i in range(0, len(text), 2):
            result += decrypt_pair(matrix, text[i:i + 2])
        return result.replace('x', '')  # Remove 'x' added as filler


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: playfair.py <keyword> <enc/dec>")
        sys.exit(1)

    keyword = sys.argv[1].lower()
    mode = sys.argv[2]

    if mode not in ['enc', 'dec']:
        print("Error: mode should be 'enc' for encryption or 'dec' for decryption.")
        sys.exit(1)

    text = input("Enter the text to be processed: ").lower()
    result = playfair_cipher(keyword, text, mode)
    print("Result:", result)
