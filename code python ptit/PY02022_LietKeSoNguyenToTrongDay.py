import math

def snt(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: 
            return 0
    return 1

n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if snt(i) and i not in b:
        b.append(i)
        print(i, a.count(i), sep=' ')