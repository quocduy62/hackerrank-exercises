import numpy as np
arr = []
n, m = list(map(int, input().split()))
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.around(np.std(arr),11))