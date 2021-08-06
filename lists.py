n = int(input())
arr = []
for _ in range(n):
    commands = input().strip().split()
    if 'insert' in commands:
        arr.insert(int(commands[1]),int(commands[2]))
    elif 'print' in commands:
        print(arr)
    elif 'remove' in commands:
        arr.remove(int(commands[1]))
    elif 'append' in commands:
        arr.append(int(commands[1]))
    elif 'sort' in commands:
        arr.sort()
    elif 'pop' in commands:
        arr.pop()
    elif 'reverse' in commands:
        arr.reverse()