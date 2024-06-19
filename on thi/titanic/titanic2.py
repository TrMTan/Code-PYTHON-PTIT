import csv

f = open(r"E:\code python\on thi\titanic\titanic.csv", "r")
data = csv.reader(f)
row = [i for i in data]
print(len(row), len(row[0]))