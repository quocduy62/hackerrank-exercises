n = int(input())
my_list = list(map(int, input().split()))
result = min(my_list)
for element in my_list:
    if element > result and element is not max(my_list):
        result = element
print(result)