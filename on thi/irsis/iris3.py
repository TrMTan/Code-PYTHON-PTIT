import csv

f = open(r"E:\code python\on thi\irsis\iris.csv")
data = csv.reader(f)
row = [i for i in data] 
thuoctinh = {"sepal_length": 0, "sepal_width": 1, "petal_length": 2, "petal_width": 3}
for i in range(int(input())):
    u, v = [], []
    name = input().lower()
    s = input().split()
    if s[0] not in thuoctinh and s[1] not in thuoctinh:
        print("Invalid")
        break
    ok = 0 # kiem tra ten loai hoa
    x = thuoctinh[s[0]] # lay vi tri cua thuoc tinh
    y = thuoctinh[s[1]] # lay vi tri cua thuoc tinh
    for i in row[1:]:
        if i[4] == name:
            u.append(float(i[x])) # them gia tri thuoc tinh vao u
            v.append(float(i[y])) # them gia tri thuoc tinh vao v
            ok = 1
    if ok == 0 or len(u) == 0 or len(v) == 0:
        print("Invalid")
    else:
        s = 0
        for i, j in zip(u, v):
            s += i * j
        print("{:.4f}".format(s))   