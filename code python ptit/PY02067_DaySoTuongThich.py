def check(p): 
    for i in a: 
        if int(i / p) == int(i / (p + 1)): # nếu a[i] / p == a[i] / (p + 1)
            return 0
    return 1

n = int(input())
a = list(map(int, input().split())) 
s = min(a) # lấy số nhỏ nhất trong dãy
kq = 0
for i in range(s, 0, -1): # duyệt từ số nhỏ nhất đến 1
    if check(i): # nếu hàm check trả về 1
        for j in range(n): # duyệt từ 0 đến n
            kq += int(a[j] / (i + 1)) + 1
        break
print(kq)