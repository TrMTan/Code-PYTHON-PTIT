def check(n):
    s = 0
    for i in range(len(n)):
        if not n[i].isdigit(): 
            return False
        else: 
            s += int(n[i])
    if s != 5: return False
    for i in range(len(n)):
        if n[i] != "0" and n[i] != "1" and n[i] != "2" and n[i] != "3" and n[i] != "4":
            return False
    return True

for i in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO") 