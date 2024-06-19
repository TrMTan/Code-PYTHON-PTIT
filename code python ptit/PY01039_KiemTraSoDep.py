def kt(s):
    for i in range(2, len(s)):
        if s[i] != s[i - 2]:
            return "NO"
    return "YES"

for i in range(int(input())):
    s = input()
    print(kt(s))    