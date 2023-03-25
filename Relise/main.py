import numpy as np

def distance_matrix(graph):
    #Вычисляем матрицу расстояний
    n = len(graph)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = np.inf
    return dist

def klein(graph):
    #Вычисляем кратчайший гамильтонов цикл для данного графа с использованием метода Клейна.
    n = len(graph)
    dist = distance_matrix(graph)
    dp = np.zeros((1 << n, n))
    parent = np.zeros((1 << n, n), dtype=int)
    for mask in range(1, 1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            if mask == (1 << last):
                dp[mask][last] = 0
                continue
            dp[mask][last] = np.inf
            for second_last in range(n):
                if not (mask & (1 << second_last)) or last == second_last:
                    continue
                val = dp[mask ^ (1 << last)][second_last] + dist[second_last][last]
                if dp[mask][last] > val:
                    dp[mask][last] = val
                    parent[mask][last] = second_last
    #Ищем минимальный цикл
    mask = (1 << n) - 1
    last = np.argmin(dp[mask])
    path = []
    while True:
        path.append(last)
        if mask == (1 << last):
            break
        new_mask = mask ^ (1 << last)
        last, mask = parent[mask][last], new_mask
    path.reverse()
    return path, dp[(1 << n) - 1][path[0]]

graph = {
    0: {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7},
    1: {0: 2, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
    2: {0: 3, 1: 2, 3: 2, 4: 3, 5: 4, 6: 5},
    3: {0: 4, 1: 3, 2: 2, 4: 2, 5: 3, 6: 4},
    4: {0: 5, 1: 4, 2: 3, 3: 2, 5: 2, 6: 3},
    5: {0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 6: 2},
    6: {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2}
}

path, length = klein(graph)
print("Минимальный путь:", path)
print("Длина:", length)

