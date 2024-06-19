while 1:
    n = int(input())
    if n == 0: break
    minN = 1e99
    maxN = 0
    for i in range(n):
        x = int(input())
        if x < minN: minN = x
        if x > maxN: maxN = x
    if minN == maxN: 
        print("BANG NHAU")
    else: 
        print(minN, maxN)    

  
                