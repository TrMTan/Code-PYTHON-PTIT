n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [[] for _ in range(n)]

for i in range(n):
    c[i] = [a[i], b[i]]

c.sort(key=lambda x: x[0] - x[1]) # sắp xếp theo a[i] - b[i]
i, res = 0, 0
while i < n:
    if k > 0:
        res += c[i][0] # cộng a[i] vào res
        k -= 1
    else:
        if c[i][0] < c[i][1]: # nếu a[i] < b[i] thì cộng a[i] vào res
            res += c[i][0] 
        else: 
            res += c[i][1] # ngược lại cộng b[i] vào res
    i += 1
print(res)

# 5 4
# 3 4 7 10 3
# 4 5 5 12 5