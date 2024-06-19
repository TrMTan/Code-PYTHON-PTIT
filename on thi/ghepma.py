f1 = open("DATA1.in", "r")
a = set(i.strip() for i in f1.readlines())
f2 = open("DATA2.in", "r")
b = set(i.strip() for i in f2.readlines())
c = []
for i in a:
    for j in b:
        c.append(i + j)
for i in sorted(c):
    print(i)