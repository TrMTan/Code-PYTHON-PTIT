from sys import setrecursionlimit

n = int(input())
setrecursionlimit(pow(10, 5) + 1) # dat gioi han do sau de tranh loi RecursionError
ke = [[] for _ in range(2 * n + 1)] # danh sach ke
color = [0] * (2 * n + 1) # 0: chua xet, 1: dang xet, 2: da xet
Name, val = {}, 1 # Name: ten thanh so, val: so thanh phan lien thong

def DFS(u): 
    color[u] = 1
    for v in ke[u]:
        if not color[v]:
            if DFS(v): return True
        elif color[v] == 1: return True
    color[u] = 2
    return False

def solve():
    for i in range(1, val): # duyet cac thanh phan lien thong
        if not color[i]: # neu chua xet
            if DFS(i): return "impossible" # neu co chu trinh
    return "possible" # neu khong co chu trinh

for _ in range(n):
    a = input().split()
    if a[0] not in Name:
        Name[a[0]] = val # gan ten thanh so
        val += 1 # tang so thanh phan lien thong
    if a[2] not in Name: 
        Name[a[2]] = val # gan ten thanh so
        val += 1 # tang so thanh phan lien thong
    if a[1] == '>': ke[Name[a[0]]].append(Name[a[2]]) # them canh u -> v vao danh sach ke
    else: ke[Name[a[2]]].append(Name[a[0]]) # them canh v -> u vao danh sach ke
print(solve())

# 3
# An > Binh
# Binh > Cong
# An < Cong