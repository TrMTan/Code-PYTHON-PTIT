for t in range(int(input())):
    s = input()
    n = input()
    l, cnt, tk = len(n), 0, s.find(n)
    while tk != -1:
        cnt += 1
        tk = s.find(n, tk + l)
    print(cnt)    