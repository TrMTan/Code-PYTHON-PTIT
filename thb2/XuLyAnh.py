for i in range(int(input())):
    n, m, l = map(int, input().split())
    a = [[0] * (m + 1)]
    for i in range(n):
        a.append([0] + list(map(int, input().split())))
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][j] += a[i - 1][j]
    
    new_a = []

    for i in range(1, n - l + 2):
        arr, s = [], 0
        for j in range(1, l + 1):
            s += a[i + l - 1][j] - a[i - 1][j]
        arr.append(s)
        for j in range(2, m - l + 2):
            s = s + (a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1]) - (a[i + l - 1][j - 1] - a[i - 1][j - 1])
            arr.append(s)
        new_a.append(arr)
    
    l *= l
    for i in new_a:
        for j in i:
            print(j // l, end=' ')
        print()
    