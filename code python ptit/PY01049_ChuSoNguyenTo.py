import math

def snt(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    n = input()
    a = list(int(i) for i in n)
    nt, l = 0, len(n)
    for i in a:
        nt += snt(int(i))
    print("YES" if snt(l) and nt > l - nt else "NO")