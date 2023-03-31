num_alphabets = int(input())
alphabet_rows = list(map(int, input().split()))
row_numbers = list(map(int, input().split()))
num_strings = int(input())
string_numbers = list(map(int, input().split()))

alphabet_mapper = dict(zip(alphabet_rows, row_numbers))

difference_counter = 0
for i in range(num_strings - 1):
    current_row = alphabet_mapper[string_numbers[i]]
    next_row = alphabet_mapper[string_numbers[i+1]]
    if current_row != next_row:
        difference_counter += 1

print(difference_counter)
