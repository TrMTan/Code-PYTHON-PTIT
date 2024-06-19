for t in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    kq = "YES"
    for i in range(n):
        if a[i] > b[i]:
            kq = "NO"
            break    
    print(kq)        