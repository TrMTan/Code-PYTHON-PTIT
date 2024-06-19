import json

f = open(r"E:\code python\on thi\flights\filghts.json", "r")
data = json.load(f)

for i in range(int(input())):
    s = input().split()
    tong = []
    for i in data["flights"]:
        if i["year"] == s[0]:
            tong.append(int(i["passengers"]))
    if s[1] == "sum": print(sum(tong))
    elif s[1] == "avg": print("{:.5f}".format(sum(tong) / len(tong)))
    elif s[1] == "min": print(min(tong))
    elif s[1] == "max": print(max(tong))