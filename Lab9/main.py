from math import sqrt

print('Введите интенсивность спроса')
v = int(input())
print('Введите затраты на хранение')
s = float(input())
print('Введите затраты на осуществление перевозок')
K = int(input())
Q = sqrt((2 * K * v)/s)
print('Оптимальный размер заказа')
print(Q)
print('Наша стратегия')
print(v/Q)