from itertools import product

n = int(input())
dice = list(product(*[list(map(int, input().split())) for _ in range(n)]))

print(len(set(map(sum, dice))))