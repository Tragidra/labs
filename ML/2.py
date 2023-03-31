with open('input.txt', 'r') as f:
    n, *heights = map(int, f.readline().split())

max_height = 0

max_left = [0] * n
max_right = [0] * n

max_left[0] = heights[0]
for i in range(1, n):
    max_left[i] = max(max_left[i-1], heights[i])

max_right[n-1] = heights[n-1]
for i in range(n-2, -1, -1):
    max_right[i] = max(max_right[i+1], heights[i])

for i in range(1, n-1):
    if min(max_left[i-1], max_right[i+1]) < heights[i]:
        continue

    height = min(max_left[i-1], max_right[i+1]) - heights[i]
    max_height = max(max_height, height)

with open('output.txt', 'w') as f:
    f.write(str(max_height))