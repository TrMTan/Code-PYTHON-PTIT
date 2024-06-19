f = open("DATA.in", "r")
n = int(f.readline().strip())
for i in range(n):
    s1 = f.readline().strip()
    s2 = f.readline().strip()
    positions = []
    len_s1 = len(s1)
    len_s2 = len(s2)
    for i in range(len_s1 - len_s2 + 1):
        if s1[i:i + len_s2] == s2:
            positions.append(i + 1)
    print(positions)