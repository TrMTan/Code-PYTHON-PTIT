import math

for t in range(int(input())):
    n = input()
    a = n[::-1]
    print("YES" if math.gcd(int(n), int(a)) == 1 else "NO")