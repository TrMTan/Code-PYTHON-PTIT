for i in range(int(input())):
    n = input()
    t = 1
    for i in range(len(n)):
        if int(i) != 0:
            t *= int(i)
    print(t)    
    