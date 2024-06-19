import math

def snt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1    

for t in range(int(input())):
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    c = math.gcd(a, b)
    tong = 0
    for i in range(0, len(str(c))):
        tong += int(str(c)[i])
    print("YES" if snt(tong) else "NO")