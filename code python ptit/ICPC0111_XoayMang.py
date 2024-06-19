for t in range(int(input())):
    n, d = [int(x) for x in input().split()]
    a = input().split()
    print(*a[d:] + a[:d])