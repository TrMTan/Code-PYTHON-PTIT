import csv 

f = open(r"E:\code python\on thi\irsis\iris.csv", "r")
data = csv.reader(f)
row = [i for i in data]

for i in range(int(input())):
    s = input().split()
    hoa = []
    for i in row[1:]:
        if i[4] == s[0] and i[2] == s[1]:
            hoa.append(float(i[0]))
    if len(hoa) == 0: print("Invalid")
    else: print("{:.4f}".format(sum(hoa) / len(hoa)))