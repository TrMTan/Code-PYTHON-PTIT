import json

f = open(r"E:\code python\on thi\flights\filghts.json", "r")
data = json.load(f)
for i in range(int(input())):
    s = input().split()
    tong = 0
    for i in data["flights"]:
        if i["year"] >= s[0] and i["year"] <= s[1]:
            tong += int(i["passengers"])
    if tong == 0:print("Invalid")
    else: print(tong)