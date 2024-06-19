a, k, n = [int(x) for x in input().split()]
kt = 0

i = 1
while True:
    if k * i > n: break
    if k * i - a > 0:
        print(k * i - a, end=" ")
        kt = 1
    i += 1    
if kt == 0: print(-1)        

# a + b <= n
# (a + b) % k = 0