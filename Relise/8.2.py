# Дописать третий шан

# находис путь
def dfs(C, F, s, t):
    stack = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while (stack):
        u = stack.pop()
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                print(paths)
                if v == t:
                    return paths[v]
                stack.append(v)
    return None


def max_flow(C, s, t):
    n = len(C)  # Конкретно тут C это матрица со значениями
    F = [[0] * n for i in range(n)]
    path = dfs(C, F, s, t)
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = dfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


#график пропускной способности

C = [[0, 4, 3, 4, 0, 0, 0],
     [0, 0, 2, 0, 0, 3, 0],
     [0, 2, 0, 3, 1, 2, 0],
     [0, 0, 3, 0, 2, 0, 5],  #Как в прошлой программе, только не забыть рассказать про особенности графа
     [0, 0, 1, 2, 0, 0, 2],
     [0, 3, 2, 0, 0, 0, 3],
     [0, 0, 0, 0, 0, 0, 0]]

source = 0
sink = 6
max_flow_value = max_flow(C, source, sink)
print("Максимальное значение пути", max_flow_value)
