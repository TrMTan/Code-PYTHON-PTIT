for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(key=lambda x: (sum(int(i) for i in str(x)), len(str(x)), x))
    print(*a)