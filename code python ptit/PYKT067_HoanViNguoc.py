import itertools

def sinh(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    d = list(itertools.permutations(l))
    d.reverse()
    return d

for t in range(int(input())):
    n = int(input())
    d = sinh(n)
    print(len(d))
    for i in d:
        print(*i, end=' ', sep='')
    print()