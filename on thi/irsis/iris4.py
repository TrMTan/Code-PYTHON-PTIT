import csv

f = open(r"E:\code python\on thi\irsis\iris1.csv")
row = [i for i in csv.reader(f)]

class Pair:
    def __init__(self, count):
        self.count = count
        self.a = []

thuoctinh = {"sepal_length": 0, "sepal_width": 1, "petal_length": 2, "petal_width": 3}
for i in range(int(input())):
    s = input().strip()
    s1 = {}
    for i in row[1:]:
        if i[thuoctinh[s]] is not None and i[4] not in s1:
            s1[i[4]] = Pair(1)
            s1[i[4]].a.append(float(i[thuoctinh[s]]))
        elif i[thuoctinh[s]] is not None and i[4] in s1:
            s1[i[4]].count += 1
            s1[i[4]].a.append(float(i[thuoctinh[s]]))
    s1 = dict(sorted(s1.items(), key = lambda x:x[0]))
    for hoa, pair in s1.items():
        tb = round(sum(pair.a) / len(pair.a), 1)
        lon = max(pair.a)
        nho = min(pair.a)
        print(f"{hoa} {pair.count} {tb:.1f} {lon:.1f} {nho:.1f}")