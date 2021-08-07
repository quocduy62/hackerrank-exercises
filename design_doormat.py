w = 'WELCOME'
c = '.|.'
d = '-'
n,m = list(map(int, input().split()))
for i in range(n//2):
    print((c*(2*i+1)).center(m, d))
print(w.center(m,d))
for i in range(n//2):
    print((c*(n-(2*i+2))).center(m, d))

