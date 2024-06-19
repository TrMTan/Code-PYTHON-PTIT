for i in range(int(input())):
    s1, s2 = input(), input()
    if sorted(s1) == sorted(s2):
        check = "YES"
    else:
        check = "NO"
    print("Test " + str(i + 1) + ": " + check)