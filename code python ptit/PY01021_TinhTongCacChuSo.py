for t in range(int(input())):
    s = input()
    t = 0
    b = []
    for i in range(len(s)):
        if s[i].isdigit():
            t += int(s[i])
        if s[i].isalpha():
            b.append(s[i])
    b.sort()            
    print(''.join(b) + str(t))
    