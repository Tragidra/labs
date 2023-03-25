def set_info():
    for i in range(n):
        points.append(list(map(int, input().split())))
    for i in range(n):
        result.append([i, points[i][1]])


n, s = map(int, input().split())
points = []
sum = 0
result = []
set_info()
#ждём равенства баллов, считая промежуточные баллы и сравнивая с итоговыми, потом сортируем и отбираем баллы
while sum != s:
    sum = 0
    for i in range(n):
        sum += result[i][1]
    result.sort(key=lambda x: x[1])
    for i in range(n):
        if result[i][1] - points[result[i][0]][0] != 0 and i != n // 2:
            result[i][1] = result[i][1] - 1
            break

result = result[n // 2][1]
print(result)