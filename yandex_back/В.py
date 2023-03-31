N = int(input())
a = [list(map(int, input().split())) for _ in range(3)]

d1 = {}
for i in range(N):
    d1[i + 1] = [elem[i] for elem in a]

Q = int(input())
a = [list(map(int, input().split())) for _ in range(3)]

d2 = {}
for i in range(Q):
    d2[i + 1] = [elem[i] for elem in a]

arr = []

for i in d2:
    aa = list()

    for j in d1:
        if (d2[i][0] == 0 and d2[i][1] == 0 and d2[i][2] == 0):
            if d1[j][0] == 0 and d1[j][1] == 0 and (d1[j][2] == 0 or d1[j][2] == 1):
                aa.append(j)
                break

        if (((d2[i][0] >= d1[j][0]) and (d2[i][1] - d1[j][1] >= 0)) or ((d2[i][2] == j) and (d1[j][2] == 1))):
            aa.append(j)
            break

    if len(aa) == 0:
        arr.append(0)
    else:
        arr.append(aa[0])

ans_str = ' '.join(map(str, arr))
print(ans_str)