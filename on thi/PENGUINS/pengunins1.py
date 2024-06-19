import csv

with open(r"E:\code python\on thi\PENGUINS\penguins.csv") as f:
    f1 = csv.reader(f)
    row = [i for i in f1]

for i in range(int(input())):
    s = input().split()
    dc = []
    sc = []
    for i in row[1:]:
        if i[0] == s[0] and i[1] == s[1]:
            if i[2] != "": dc.append(float(i[2]))
            if i[3] != "": sc.append(float(i[3]))
    if len(dc) == 0 and len(sc) == 0:
        print("Invalid")
    else:
        dctb = round(sum(dc) / len(dc), 4)
        sctb = round(sum(sc) / len(sc), 4)
        print(f"{dctb} {sctb}")