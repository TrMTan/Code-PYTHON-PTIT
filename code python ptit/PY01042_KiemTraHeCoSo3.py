def kt(s):
    for i in range(len(s)):
        if s[i] >'2' or s[i] < '0':
            return "NO"
    return "YES"

for i in range(int(input())):
    s = input()
    print(kt(s))