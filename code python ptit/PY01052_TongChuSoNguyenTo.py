import math

def snt(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return "NO"
    return "YES"

for t in range(int(input())):
    n = input()
    s = sum(int(i) for i in n)
    print(snt(s))