import math
#to hop
n = int(input())
res = [list(input()) for _ in range(n)]
hang = [0] * n
cot = [0] * n
for i in range(n):
    for j in range(n):
        hang[i] += res[i][j].count('C')
        cot[j] += res[i][j].count('C')
kq = 0
for i in range(n):
    if hang[i] > 1: kq += math.comb(hang[i], 2)
    if cot[i] > 1: kq += math.comb(cot[i], 2)
print(kq) 