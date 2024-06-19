for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    kq = 0
    for i in range(n - 1):
        l = min(a[i], a[i + 1])
        r = max(a[i], a[i + 1])
        while r > 2 * l: 
            kq += 1
            l *= 2
    print(kq)

# 6
# 4
# 4 2 10 1
# 2
# 1 3
# 2
# 6 1
# 3
# 1 4 2
# 5
# 1 2 3 4 3
# 12
# 4 31 25 50 30 20 34 46 42 16 15 16