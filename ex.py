import numpy as np

arr = []
n,m =  list(map(int, input().split()))
for row in range(n):
    element_arr = list(map(int, input().split()))
    arr.append(element_arr)
# last_arr = np.array(arr)
# print(np.min(arr,axis=1))
print(max(np.min(arr,axis=1)))