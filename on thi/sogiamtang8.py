def tang(s):
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]: return False
    return True 
def giam(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]: return False
    return True

for i in range(int(input())):
    n = input()
    if len(n) > 8: 
        print("NO")
    ok = 0
    for i in range(len(n)):
        if tang(n[:i]) and giam(n[i:]):
            ok = 1
    if ok: print("YES") 
    else: print("NO")