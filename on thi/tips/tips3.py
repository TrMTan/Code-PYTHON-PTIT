import json

f = open(r"E:\code python\on thi\tips\tips.json", "r") 
data = json.load(f)
for i in range(int(input())):
    s = input().split()
    tong = []
    for i in data["tips"]:
        if i["day"] == s[0] and i["size"] == s[1]:
            tong.append(float(i["total_bill"]))
    if len(tong) == 0: print("Invalid")
    else: print("{:.4f}".format(sum(tong)/len(tong)))