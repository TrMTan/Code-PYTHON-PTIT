import math

def snt(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return "NO"
    return "YES" if n > 1 else "NO"

for t in range(int(input())):
    n = input()
    s = int(n[-4:])
    print(snt(s))