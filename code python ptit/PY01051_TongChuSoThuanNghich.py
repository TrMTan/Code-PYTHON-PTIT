for i in range(int(input())):
    s = str(sum(int(i) for i in input()))
    print("YES" if s == s[::-1] and len(s) > 1 else "NO")
    