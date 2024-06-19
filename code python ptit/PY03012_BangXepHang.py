n = int(input())
a = []
for i in range(n):
    ht = input()
    ac, sub = [int(x) for x in input().split()]
    a.append((ht, ac, sub))

a.sort(key = lambda x: (-x[1], x[2], x[0])) # sắp xếp theo thứ tự giảm dần của ac, tăng dần của sub, tăng dần của ht
for i in a:
    print(i[0], i[1], i[2])    