for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    res = 0
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                res += 1
                l += 1
            elif a[i] + a[l] + a[r] > 0:
                r -= 1
            else:
                l += 1
    print(res)                    