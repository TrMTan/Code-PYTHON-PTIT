def rotate(s):
    r = ''
    sum = 0
    for i in s: sum += ord(i) - ord('A')
    for i in s: r += chr((ord(i) - ord('A') + sum) % 26 + ord('A'))
    return r

for t in range(int(input())):
    s = input()
    r = ''
    a, b = rotate(s[:len(s)//2]), rotate(s[len(s)//2:])
    for i in range(len(a)):
        r += chr(((ord(a[i]) - ord('A')) + (ord(b[i]) - ord('A'))) % 26 + ord('A'))
    print(r)