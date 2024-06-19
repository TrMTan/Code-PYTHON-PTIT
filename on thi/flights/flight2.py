import json

f = open(r"E:\code python\on thi\flights\filghts.json", "r")
data = json.load(f)
print(len(data["flights"]), len(data["flights"][0]))