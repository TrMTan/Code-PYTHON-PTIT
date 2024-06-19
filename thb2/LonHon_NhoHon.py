from sys import setrecursionlimit

setrecursionlimit(pow(10, 5) + 1)
n = int(input())
ke = [[] for _ in range(2 * n + 1)]
color = [0] * (2 * n + 1)
name, lt = {}, 1

def DFS(u):
    color[u] = 1
    for v in ke[u]:
        if not color[v]:
            if DFS(v): return True
        elif color[v] == 1: return True
    color[u] = 2
    return False

def solve():
    for i in range(1, lt):
        if not color[i]:
            if DFS(i): return "impossible"
    return "possible"

for _ in range(n):
    a = input().split()
    if a[0] not in name:
        name[a[0]] = lt
        lt += 1
    if a[2] not in name:
        name[a[2]] = lt
        lt += 1
    if a[1] == '>': ke[name[a[0]]].append(name[a[2]])
    else: ke[name[a[2]]].append(name[a[0]])
print(solve())