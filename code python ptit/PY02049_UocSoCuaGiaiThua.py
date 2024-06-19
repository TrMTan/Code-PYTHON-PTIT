for i in range(int(input())):
    n, p = map(int, input().split())
    x = 0
    for i in range(1, n + 1):
        while i % p == 0:
            x += 1
            i //= p
    print(x)