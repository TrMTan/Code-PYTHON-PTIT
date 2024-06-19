for t in range(int(input())):
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = [float(x) for x in input().split()]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))