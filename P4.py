#Write a program to implement Playfair cipher.

def create_key_table(key):
    key = key.upper().replace("J", "I")
    table = []

    for char in key:
        if char not in table and char.isalpha():
            table.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in table:
            table.append(char)

    return [table[i:i+5] for i in range(0, 25, 5)]


def find_position(table, char):
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                return i, j


def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0

    while i < len(plaintext):
        a = plaintext[i]
        b = ""

        if i + 1 < len(plaintext):
            b = plaintext[i+1]
            if a == b:
                b = "X"
                i += 1
            else:
                i += 2
        else:
            b = "X"
            i += 1

        pairs.append(a + b)

    return pairs


def playfair_cipher(plaintext, key):
    key_table = create_key_table(key)
    pairs = prepare_text(plaintext)

    ciphertext = ""

    for pair in pairs:
        r1, c1 = find_position(key_table, pair[0])
        r2, c2 = find_position(key_table, pair[1])

        if r1 == r2:  # Same row
            ciphertext += key_table[r1][(c1+1) % 5]
            ciphertext += key_table[r2][(c2+1) % 5]

        elif c1 == c2:  # Same column
            ciphertext += key_table[(r1+1) % 5][c1]
            ciphertext += key_table[(r2+1) % 5][c2]

        else:  # Rectangle rule
            ciphertext += key_table[r1][c2]
            ciphertext += key_table[r2][c1]

    return ciphertext


# Main
plaintext = "HELLO WORLD"
key = "example"

ciphertext = playfair_cipher(plaintext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
