def find_booring(data, dict):

    if len(set(data)) == len(data):
        return True

    values = list(dict.values())
    if 1 in values:
        values.remove(1)
        if len(set(values)) == 1 or len(set(values)) == 0:
            return True
        else:
            values.append(1)

    maxi = max(values)
    values[values.index(maxi)] -= 1

    if len(set(values)) == 1 or len(set(values)) == 0:
        return True
    else:
        return False

input()
a = list(map(int, input().split()))
b = (a[::-1][i:] for i in range(0, len(a[::-1])))
for i in b:
    dict1 = {num: i.count(num) for num in i}
    if find_booring(i, dict1):
        print(len(i))
        break