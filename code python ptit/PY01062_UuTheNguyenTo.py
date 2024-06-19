import math

def kt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    n = input()
    l, nt = len(n), 0
    for i in n:
        if(kt(int(i))):
            nt += 1
    print("YES" if kt(l) and nt > l - nt else "NO")        