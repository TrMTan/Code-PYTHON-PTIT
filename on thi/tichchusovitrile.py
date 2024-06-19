for i in range(int(input())):
    n = input()
    t = 1
    ok = 0
    for i, digit in enumerate(n):
        if (i + 1) % 2 != 0:
            so = int(digit)
            if so != 0:
                t *= so
                ok = 1
    if not ok: t = 0
    print(t)    