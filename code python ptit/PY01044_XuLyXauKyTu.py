a = list(input().split())
b = list(input().split())

a_set, b_set = set(), set()
for i in a: a_set.add(i.lower())
for i in b: b_set.add(i.lower())

for i in sorted(a_set.union(b_set)):
    print(i, end = ' ')
print()
for i in sorted(a_set.intersection(b_set)):
    print(i, end = ' ')
    
# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++