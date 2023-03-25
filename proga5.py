def razum(a):
    for i in range(n - 1): #ищем разумные отрезки
        for j in range(i + 1, n):
            if sum(balance[i:j + 1]) == 0:
                a.append([i, j])

def count_norm():
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if any(i <= a[k][0] and j >= a[k][1] for k in range(len(a))):
                count += 1
    return count

n = int(input())
balance = list(map(int, input().split()))
a = [] #разумные
razum(a)
count_norm()
print(count_norm())