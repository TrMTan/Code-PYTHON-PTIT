for t in range(int(input())):
    s = input()
    print("YES" if s[:2] == s[-2:] else "NO")