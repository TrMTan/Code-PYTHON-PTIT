for t in range(int(input())):
    a, b = [x for x in input().split()]
    n = input().strip()
    if n.count(' '): n, m = n.split()
    else: m = input()
    p = min(a, b)
    q = max(a, b)
    print(str(int(n.replace(q, p)) + int(m.replace(q, p))), str(int(n.replace(p, q)) + int(m.replace(p, q))))
