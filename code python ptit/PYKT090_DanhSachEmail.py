f = open("CONTACT.in", "r")

a = set()
for i in f:
    a.add(i.rstrip('\n').lower())
a = sorted(a)
for i in a:
    print(i)