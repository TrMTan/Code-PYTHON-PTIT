import math

def snt(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    for i in n:
        if not snt(int(i)):
            return "No"
    s = sum(int(i) for i in n)        
    n1, n2 = n, n[::-1]
    if not snt(int(n1)) or not snt(int(n2)) or not snt(s):
        return "No"    
    return "Yes"
    
for t in range(int(input())):
    n = input()
    print(check(n))    
        