n = int(input())
s = input()

if 'a' not in s or 'b' not in s or 'c' not in s or 'd' not in s:
    print(-1)  # Сразу убираем варианты когда у нас в строке не все символы
else:
    ans = n
    i, j = 0, 0
    count = {'a':0, 'b':0, 'c':0, 'd':0}  #Считаем количество вхождени символа в подстроку

    while j < n:
        count[s[j]] += 1  #закидываем символ в словарт выше
        j += 1

        while all(count.values()):
            ans = min(ans, j-i)  #ищем минимальную длину хорошей подстроки
            count[s[i]] -= 1  #удаляем первый символ подстроки из словаря
            i += 1

    print(ans)