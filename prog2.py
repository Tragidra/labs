n, m, k = map(int, input().split())

programs_per_senior = (n*k + m - 1) // m

total_time = programs_per_senior

print(total_time)