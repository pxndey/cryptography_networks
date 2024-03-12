def create_matrix(key):
    key = key.replace(" ", "").upper()
    matrix = []
    letters_added = []

    for char in key:
        if char not in letters_added:
            if char != 'J':
                letters_added.append(char)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in letters_added:
            letters_added.append(char)

    for i in range(5):
        row = []
        for j in range(5):
            row.append(letters_added[i * 5 + j])
        matrix.append(row)

    return matrix

def find_position(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % 2 != 0:
        plaintext += "X"

    matrix = create_matrix(key)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]

        if char1 == char2:
            char2 = "X"
            plaintext = plaintext[:i + 1] + "X" + plaintext[i + 1:]

        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        ciphertext += matrix[row1][col1] + matrix[row2][col2]

    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    matrix = create_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]

        row1, col1 = find_position(char1, matrix)
        row2, col2 = find_position(char2, matrix)

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        plaintext += matrix[row1][col1] + matrix[row2][col2]

    plaintext = plaintext.replace("X", "")
    return plaintext

# User input
choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
text = input("Enter the text: ")
key = input("Enter the key: ")

if choice == 'E':
    result = encrypt(text, key)
    print(f"Ciphertext: {result}")
elif choice == 'D':
    result = decrypt(text, key)
    print(f"Plaintext: {result}")
else:
    print("Invalid choice. Please try again.")