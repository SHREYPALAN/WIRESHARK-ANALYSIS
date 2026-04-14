def print_rail_fence_pattern(text, rails):
    text = text.replace(" ", "")
    n = len(text)

    # Create matrix filled with spaces
    fence = [[" " for _ in range(n)] for _ in range(rails)]

    row, col = 0, 0
    direction = 1  # 1 = down, -1 = up

    # Fill the pattern
    for char in text:
        fence[row][col] = char
        col += 1
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    # Print the pattern
    for r in fence:
        print("".join(r))


# Main
plaintext = "HELLO WORLD"
rails = 3

print_rail_fence_pattern(plaintext, rails)
