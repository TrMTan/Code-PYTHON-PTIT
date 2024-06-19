for t in range(int(input())):
    n = input()
    if len(n) == 1: print(n)
    else:
        i, lt, res = len(n) -1, 0, ""
        while i > 0:
            tmp = int(n[i]) + lt
            lt = 1 if tmp >= 5 else 0
            res = "0" + res
            i -= 1
        res = str(int(n[i]) + lt) + res
        print(res)    