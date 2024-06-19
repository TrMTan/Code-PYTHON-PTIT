def kt(a):
    if len(a) != 4:
        return False
    for i in a:
        if not str(i).isnumeric():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True

for i in range(int(input())):
    a = input().split('.')
    print('YES' if kt(a) else 'NO')
 