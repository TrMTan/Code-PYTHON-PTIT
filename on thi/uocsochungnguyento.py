from math import sqrt, gcd
def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def check(a, b):
    c = gcd(a, b)
    tong = 0
    for i in range(len(str(c))):
        tong += int(str(c)[i])
    if snt(tong): return "YES"
    else: return "NO"

for i in range(int(input())):
    a, b = map(int, input().split())
    print(check(a, b))