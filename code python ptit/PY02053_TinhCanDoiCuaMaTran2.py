n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(j) for j in input().split()]

ntren, nduoi = 0, 0
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            ntren += a[i][j]
        elif j < n - i - 1:
            nduoi += a[i][j]

k = int(input())
sub = abs(ntren - nduoi)
print("YES" if sub <= k else "NO")
print(sub)                    
