import math

sang = [1] * 10000
sang[0] = sang[1] = 0
for i in range(2, 101):
    if sang[i] == 1:
        for j in range(i * i, 10000, i):
            sang[j] = 0

prime = [0]
for i in range(2, 10000):
    if sang[i] == 1:
        prime.append(i)

n, x = [int(i) for i in input().split()]
for i in range(n + 1):
    x += prime[i]
    print(x, end=' ')
