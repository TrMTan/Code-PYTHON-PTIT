import math

def snt(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    n = int(input())
    k = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            k += 1
    if snt(k):
        print("YES")    
    else:
        print("NO")                