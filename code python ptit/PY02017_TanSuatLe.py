for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = set(a)
    for i in b:
        if a.count(i) % 2 == 1:
            print(i)
            break
     
    