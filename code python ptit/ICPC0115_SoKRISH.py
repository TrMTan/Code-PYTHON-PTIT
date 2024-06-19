a = [1] * 10
for i in range(2, 10):
    a[i] = a[i-1] * i

for t in range(int(input())):
    n = input()
    s = sum(a[int(i)] for i in n)    
    print("Yes" if s == int(n) else "No")    