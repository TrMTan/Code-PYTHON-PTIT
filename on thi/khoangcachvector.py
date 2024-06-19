import math

for i in range(int(input())):
    s = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    kq = 0
    if len(a) != len(b):
        print("Invalid")
        break
    if s == "euclidean":
        for i, j in zip(a, b):
            kq += (i - j) ** 2
        kq = math.sqrt(kq)
    elif s == "manhattan":
        for i, j in zip(a, b):
            kq += abs(i - j)
    elif s == "minkowski":
        hop = set(a).intersection(set(b))
        giao = set(a).union(set(b))
        Jac = len(hop) / len(giao)
        if Jac == 0:
            print("Invalid")
            break
        for i, j in zip(a, b):
            kq += abs(i - j) ** Jac
        kq = kq * float(1 / Jac)
    print(f'{kq:.5f}')