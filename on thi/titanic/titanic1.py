import csv

with open(r"E:\code python\on thi\titanic\titanic.csv") as f:
    f1 = csv.reader(f)
    row = [i for i in f1]

for t in range(int(input())):
    s = input().split()
    csong, cchet = 0, 0
    for i in row[1:]:
        if i[1] == s[0] and i[2] == s[1]:
            if int(i[0]) == 0: cchet += 1
            elif int(i[0]) == 1: csong += 1
    if csong == 0 and cchet == 0: print("Invalid")
    else: print(f"{cchet} {csong}")