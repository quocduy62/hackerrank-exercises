import numpy as np

arr = []
n, m = list(map(int, input().split()))
for _ in range(n):
    arr.append(list(map(int, input().split())))
# sum_arr = np.sum(arr, axis=0)
print(np.prod(np.sum(arr, axis=0)))