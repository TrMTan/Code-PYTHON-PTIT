from math import sqrt, pow
for t in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d, d1 = 0, 0
    for i, j in zip(a, b):
        d += pow(i - j, 2)
        d1 += i * j
    d = sqrt(d)
    print("{:.2f} {}".format(d, d1))