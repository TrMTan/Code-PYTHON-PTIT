for t in range(int(input())):
    s = input()
    n = input()
    l, cnt, xau = len(n), 0, s.find(n)
    while xau != -1:
        cnt += 1
        xau = s.find(n, xau + l)
    print(cnt)    