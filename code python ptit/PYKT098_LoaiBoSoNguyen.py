def check(s):
    so = 0
    for i in s:
        if not i.isdigit():
            return True
        so = so * 10 + int(i)
    if so <= 2147483647 and so >= -2147483648:
        return False
    return True

with open('DATA.in', 'r') as file:
    a = []
    for line in file:
        for i in line.split():
            if check(i):
                a.append(i)
    for i in sorted(a):
        print(i, end=' ')