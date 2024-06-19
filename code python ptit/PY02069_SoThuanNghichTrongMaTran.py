def stn(n):
    if int(n) < 10:
        return False
    return n == n[::-1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = []
for i in range(n):
    for j in range(m):
        if stn(str(a[i][j])):
            b.append(a[i][j])
if len(b) == 0: print("NOT FOUND")
else: 
    print(max(b))
    for i in range(n):
        for j in range(m):
            if a[i][j] == max(b):
                print("Vi tri [{}][{}]".format(i, j))

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77