import math

for t in range(int(input())):
    n = int(input())
    kq = "1"
    for i in range(2, int(math.sqrt(n)) + 1):
        dem = 0
        while n % i == 0:
            dem += 1
            n /= i
        if dem != 0:
            kq += " * " + str(i) + "^" + str(dem)
        if n == 1:
            break
    if n != 1:
        kq += " * " + str(int(n)) + "^1"
    print(kq)            