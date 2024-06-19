import math

n = int(input())
a = [float(i) for i in input().split()]
ma = max(a)
mi = min(a)
for i in a:
    if i == ma or i == mi:
        a.remove(i)
print("{:.2f}".format(sum(a) / len(a)))   