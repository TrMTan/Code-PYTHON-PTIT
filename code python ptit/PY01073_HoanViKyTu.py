n = input()
l = len(n)
dd = [0] * l

def sinh(s):
    if len(s) == l:
        print(s)
        return
    for i in range(l):
        if dd[i] == 0:
            dd[i] = 1
            sinh(s + n[i])
            dd[i] = 0

sinh("")