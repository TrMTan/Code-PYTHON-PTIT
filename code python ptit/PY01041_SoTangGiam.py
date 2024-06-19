def ktra(s):
    if len(s) < 3: return "NO"
    a = [int(i) for i in s]
    kt = 0
    for i in range(1, len(a)):
        if kt == 0 and a[i] <= a[i - 1]:
            kt = 1
        elif kt == 1 and a[i] >= a[i - 1]:
            return "NO"
    return "YES"        


for t in range(int(input())):
    n = input()
    print(ktra(n))
    