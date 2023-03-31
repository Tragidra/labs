import numpy as np

n, k = map(int, input().split())

# создание массива возможных значений для кубика
dice = np.arange(1, k+1)

# создание массива всех возможных комбинаций выпадения кубиков
combinations = np.stack(np.meshgrid(*([dice]*n)), -1).reshape(-1, n)

# умножение чисел в каждой комбинации и подсчет делителей для каждого произведения
divisors = np.sum(np.sum(np.mod(np.outer(np.prod(combinations, axis=1), np.arange(1, int(np.max(np.prod(combinations, axis=1))**0.5) + 1)) == 0, axis=1) % 2 == 1))

# вычисление вероятности победы Пети
pete_prob = (divisors / combinations.shape[0]).astype(int)

# вывод ответа в нужном формате
print((pete_prob * pow((combinations.shape[0] - pete_prob), 1000000005, 1000000007)) % 1000000007)
