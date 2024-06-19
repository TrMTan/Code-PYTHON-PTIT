p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    a = input()
    if a == "0":
        break
    k, s = a.split()
    k = int(k)
    res = ''
    for i in s:
        j = p.find(i)
        res += p[(j + k) % 28]
    print(res[::-1])