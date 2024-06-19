with open("DATA1.in", "r") as f1:
    a = f1.read()
    s1 = set([i.lower() for i in a.split()])

with open("DATA2.in", "r") as f2:
    b = f2.read()
    s2 = set([i.lower() for i in b.split()])

print(" ".join(sorted(s1.difference(s2))))
print(" ".join(sorted(s2.difference(s1))))