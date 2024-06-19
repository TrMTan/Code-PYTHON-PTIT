n = int(input())
res = []
for i in range(n):
    res.append(input())
hang = [0] * n
cot = [0] * n
for i in range(n):
    for j in range(n):
        if res[i][j] == 'C':
            hang[i] += 1
            cot[j] += 1
kq = 0
for i in range(n):
    if hang[i] > 1: kq += hang[i] * (hang[i] - 1) // 2
    if cot[i] > 1: kq += cot[i] * (cot[i] - 1) // 2
print(kq)

# 4
# CC..
# C..C
# .CC.
# .CC.