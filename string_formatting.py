def print_formatted(n):
    for i in range(1,n+1):
        print(f'{i}', end='\t')
        print(f'{oct(i).lstrip("0o")}', end='\t')
        print(f'{hex(i).upper().lstrip("0X")}', end='\t')
        print(f'{bin(i).lstrip("0b")}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
