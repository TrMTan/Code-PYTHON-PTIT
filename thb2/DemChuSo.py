def cal(a, b):
    c = []
    s = ""
    for i in range(a, b + 1):
        s += str(i)
    s = sorted(s)
    for i in range(10):
        c.append(s.count(str(i)))
    return c

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(*cal(a, b))
