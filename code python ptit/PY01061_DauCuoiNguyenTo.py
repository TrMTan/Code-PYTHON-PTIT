import math

def kt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

for t in range(int(input())):
    n = input()
    if(kt(int(n[0:3])) and kt(int(n[-3:]))):
        print("YES")
    else:
        print("NO")    