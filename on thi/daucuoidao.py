for i in range(int(input())):
    n = input()
    a = n[:2]
    b = n[-2:]
    c = b[::-1]
    print("YES" if a == c else "NO")