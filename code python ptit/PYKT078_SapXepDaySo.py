for i in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            a.insert(i, m)
            break
    for i in a:
        if i < 0:
            print(i, end=' ')
    for i in a:
        if i >= 0:
            print(i, end=' ')
    print()                        

    