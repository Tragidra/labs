n = int(input()) # ввод длины строки
s = input() # ввод строки

if 'a' not in s or 'b' not in s or 'c' not in s or 'd' not in s: # отсекаем ненужные варианты
    print(-1)
    exit()

for i in range(4, n + 1): # цикл от 4 до n. Сначала будем искать маленькие подстроки, потом больше и больше
    for j in range(n - i + 1):
        if 'a' in s[j:j + i] and 'b' in s[j:j + i] and 'c' in s[j:j + i] and 'd' in s[j:j + i]:
            print(i)
            exit()