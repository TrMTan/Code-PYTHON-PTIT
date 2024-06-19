import math

def kt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

def snt(s):
    for i in range(len(s)):
        if((kt(i) and not kt(int(s[i]))) or (not kt(i) and kt(int(s[i])))):
            return "NO"
    return "YES"        

for t in range(int(input())):
    print(snt(input())) 