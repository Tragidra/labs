N = int(input())
a = input()
a = list(map(int, a.split()))


def find_largest_difference_pair(arr):
    max_diff = -float('inf')
    max_diff_indices = None

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = arr[i] - arr[j]
            if diff > max_diff:
                max_diff = diff
                max_diff_indices = (i, j)
            elif diff == max_diff and i - j > max_diff_indices[0] - max_diff_indices[1]:
                max_diff_indices = (i, j)

    return max_diff_indices


indexes = find_largest_difference_pair(a)
if a[indexes[0]] > a[indexes[1]]:
    print(str(indexes[0]+1) + ' ' + str(indexes[1]+1))
else:
    print(str(indexes[1] + 1) + ' ' + str(indexes[0] + 1))