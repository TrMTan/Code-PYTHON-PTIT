for i in range(int(input())):
    n = input()
    tc = 0
    tl = 1
    for i in range(len(n)):
        so = int(n[i])
        if i % 2 != 0:
            tc += so
        else: 
            tl *= so
    if tc == 0: 
        print("INVALID")
    else: print("{:.06f}".format(tl/tc))   