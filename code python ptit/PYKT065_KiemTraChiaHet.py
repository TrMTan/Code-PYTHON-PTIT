import math

def check(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    s = input().split() 
    if s[0] == "-1": break
    l, r = [int(x) for x in s]
    n = int(input())
    cnt = 0
    for i in range(l, r + 1):
        if check(i) and i % n == 0:
            cnt += 1
    print(cnt)