import sys

def read_ints():
    return map(int, input().split())

def main():
    # Read input
    sym_in_line, max_s_len = read_ints()
    sym = input().strip()
    next_point = read_ints()
    s_line = read_ints()

    # Initialize variables
    letters = {chr(97+i): i for i in range(26)}
    otvet = 0

    # Iterate over positions in sym
    for i in range(len(sym)):
        symbols_positions = {}
        total_symbols = {}
        pos = i

        # Iterate over characters in the substring
        for j in range(max_s_len):
            if pos >= len(sym):
                break

            # Update symbol positions and count
            c_sum = sym[pos]
            symbols_positions[pos] = symbols_positions.get(pos, 0) + 1
            if symbols_positions[pos] > 1:
                position = (letters[c_sum] + ((symbols_positions[pos] - 1) * s_line[pos])) % 26
                c_sum = chr(97 + position)
            total_symbols[c_sum] = total_symbols.get(c_sum, 0) + 1

            # Update answer
            otvet += len(total_symbols)

            # Move to next position
            pos = next_point[pos] - 1

    # Print answer
    print(otvet)

if __name__ == "__main__":
    main()