for _ in range(int(input())):
    n, m, l = map(int, input().split())
    a = [[0] * (m + 1)] # tao ma tran a

    for i in range(n): 
        a.append([0] + list(map(int, input().split()))) # them dong vao ma tran a

    for i in range(1, n + 1):
        for j in range(1, m + 1): 
            a[i][j] += a[i - 1][j] # tinh tong cac phan tu tren cot

    new_a = [] # tao ma tran moi

    for i in range(1, n - l + 2): 
        arr, s = [], 0 # arr: mang chua cac gia tri, s: tong cac gia tri
        for j in range(1, l + 1): 
            s += a[i + l - 1][j] - a[i - 1][j] # tinh tong cac gia tri tren cot
        arr.append(s)
        for j in range(2, m - l + 2):
            s = s + (a[i + l-1][j + l - 1] - a[i - 1][j + l - 1]) - (a[i + l - 1][j - 1] - a[i - 1][j - 1]) # tinh tong cac gia tri tren cot
            arr.append(s)
        new_a.append(arr)

    l *= l # tinh l^2
    for i in new_a: 
        for j in i: 
            print(j // l, end=' ')
        print()

# 1
# 4 4 3
# 2 1 0 0
# 3 2 1 1
# 4 5 2 1
# 2 2 9 0
