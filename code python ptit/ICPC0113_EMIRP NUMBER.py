sang = [0] * 1000000

def prime():
    sang[0] = sang[1] = 0
    for i in range(2, 1000):
        if sang[i] == 0:
            for j in range(i * i, 1000000, i):
                sang[j] = 1

prime()
for t in range(int(input())):
    n = int(input())
    for i in range(2, n):
        re = int(str(i)[::-1])
        if sang[i] == 0 and sang[re] == 0 and re > i and re < n:
            print(i, re, end=' ')
    print()