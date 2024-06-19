def kt(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        rn = int(str(n)[::-1])
        n += rn
    return -1

for i in range(int(input())):
    n = int(input())
    print(kt(n))    
    