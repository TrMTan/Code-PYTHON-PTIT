# n * (1 + x%)^a = m
import math

for t in range(int(input())):
    n, x, m = [float(x) for x in input().split()]
    a = math.log(m / n, 1 + x / 100)
    print(math.ceil(a))
    
