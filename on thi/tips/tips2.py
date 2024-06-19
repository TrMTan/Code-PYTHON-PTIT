import json

f = open(r"E:\code python\on thi\tips\tips.json", "r") 
data = json.load(f)

for i in range(int(input())):
    s = input().split()
    tong = []
    for i in data["tips"]:
        if i["sex"] == s[0] and s[1] in i and i[s[1]] is not None:
            tong.append(float(i["total_bill"]))
    if len(tong) == 0: print("Invalid")
    else: print("{:.4f} {:.4f} {:.4f} {:.4f}".format(sum(tong), sum(tong) / len(tong), max(tong), min(tong)))
