import csv 

f = open(r"E:\code python\on thi\irsis\iris.csv")
data = csv.reader(f)
row = [i for i in data]

for i in range(int(input())):
    s = input().split()
    hoa = []
    if s[1] == "sepal_length":
        for i in row[1:]:
            if i[4] == s[0]:
                hoa.append(float(i[0]))
    elif s[1] == "petal_length":
        for i in row[1:]:
            if i[4] == s[0]:
                hoa.append(float(i[2]))
    if len(hoa) == 0: print("Invalid")
    else:
        if s[2] == "min": print(min(hoa))
        elif s[2] == "max": print(max(hoa))
        elif s[2] == "avg": print("{:.2f}".format(sum(hoa) / len(hoa)))
        elif s[2] == "sum": print(sum(hoa)) 