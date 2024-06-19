import itertools

n, k = [int(x) for x in input().split()]
d = {x for x in input().split()}
d = sorted(d)
l = list(itertools.combinations(d, k))
for i in l:
    print(*i, sep=' ',  end='\n')

# DONG TAY NAM BAC TAY BAC