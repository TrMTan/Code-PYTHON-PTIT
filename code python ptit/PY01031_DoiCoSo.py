f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(int(input())):
    n, b = map(int, input().split())
    res = ''
    while(n > 0):
        x = n % b
        res = f[x] + res
        n //= b
    print(res)