for t in range(int(input())):
    s = input()
    res = ''
    for i in s:
        if i.isalpha(): res += ' ' 
        else: res += i
    a = [int(i) for i in res.split()]
    print(min(a))           

# 2
# 12ab29cd19
# ab123gh456cd