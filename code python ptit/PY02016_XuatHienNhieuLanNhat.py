for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    h = n // 2 #lấy phần nguyên
    res = max(d, key=d.get) #lấy giá trị lớn nhất trong d
    if d[res] > h:
        print(res)
    else:
        print("NO")
