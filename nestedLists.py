init_arr = []
score_arr = []
result = []
n = int(input())
for _ in range(n):
    init_arr.append([input(), float(input())])
for _ in range(n):
    score_arr.append(init_arr[_][1])
min_score = min(score_arr)
while min(score_arr) == min_score:
    score_arr.remove(min(score_arr))
second_min_score = min(score_arr)
# print(second_min_score)
for _ in range(n):
    if init_arr[_][1] == second_min_score:
        result.append(init_arr[_][0])
result.sort()
for name in result:
    print(name)
