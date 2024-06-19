sang = [1]*1000000
sang[0] = sang[1] = 0
for i in range(2, 1000):
    if sang[i]:
        for j in range(i * i, 1000000, i):
            sang[j] = 0

prime = []
for i in range(1000000):
    if sang[i]:
        prime.append(i)            

for t in range(int(input())):
    n = int(input())
    cnt = 0
    for i in prime:
        if i + 6 > n:
            break
        if sang[i + 2] and sang[i + 6] or sang[i + 4] and sang[i + 6]:
            cnt += 1    
    print(cnt)        