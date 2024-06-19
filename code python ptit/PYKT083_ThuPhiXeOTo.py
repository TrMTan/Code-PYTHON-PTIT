price = {
    '5': 10000,
    '7': 15000,
    '2': 20000,
    '29': 50000,
    '45': 70000,
}

a = {}
for t in range(int(input())):
    n = input().split()
    if n[3] == 'OUT': continue
    if a.get(n[4]) is None:
        a[n[4]] = price[n[2]]
    else:
        a[n[4]] += price[n[2]]
for i in sorted(a):
    print(f'{i}: {a[i]}')
    