with open('input.txt', 'r') as f:
    num_rows = int(f.readline().strip())
    matrix_1 = [list(map(int, f.readline().strip().split())) for _ in range(3)]
    dict_1 = {}
    for i in range(num_rows):
        dict_1[i + 1] = [elem[i] for elem in matrix_1]

    num_queries = int(f.readline().strip())
    matrix_2 = [list(map(int, f.readline().strip().split())) for _ in range(3)]
    dict_2 = {}
    for i in range(num_queries):
        dict_2[i + 1] = [elem[i] for elem in matrix_2]

output_arr = []
for i in dict_2:
    indices_list = []
    for j in dict_1:
        if (dict_2[i][0] == 0 and dict_2[i][1] == 0 and dict_2[i][2] == 0):
            if dict_1[j][0] == 0 and dict_1[j][1] == 0 and (dict_1[j][2] == 0 or dict_1[j][2] == 1):
                indices_list.append(j)
                break
        if (((dict_2[i][0] >= dict_1[j][0]) and (dict_2[i][1] - dict_1[j][1] >= 0)) or ((dict_2[i][2] == j) and (dict_1[j][2] == 1))):
            indices_list.append(j)
            break
    if len(indices_list) == 0:
        output_arr.append(0)
    else:
        output_arr.append(indices_list[0])

output_str = ' '.join(map(str, output_arr))

print(output_str)
