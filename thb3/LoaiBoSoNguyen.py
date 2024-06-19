def check(s):
    x = 0
    for i in s:
        if not i.isdigit():
            return True
        x = x * 10 + int(i)
    if x <= 2147483647 and x >= -2147483648:
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
