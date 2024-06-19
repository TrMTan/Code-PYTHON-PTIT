def diem(n):
    if 0 < n < 3: return 1
    if 2 < n < 5: return 2.5
    if n < 7: return 3
    if n < 10: return 3.5
    if n < 13: return 4
    if n < 16: return 4.5
    if n < 20: return 5
    if n < 23: return 5.5
    if n < 27: return 6
    if n < 30: return 6.5
    if n < 33: return 7
    if n < 35: return 7.5
    if n < 37: return 8
    if n < 39: return 8.5
    return 9

for t in range(int(input())):
    a = [float(i) for i in input().split()]
    tb = (diem(int(a[0])) + diem(int(a[1])) + a[2] + a[3]) / 4
    if tb % 1 >= 0.75:
        tb = int(tb) + 1
    elif tb % 1 >= 0.25:
        tb = int(tb) + 0.5
    else:
        tb = int(tb)
    print('{:.1f}'.format(tb))