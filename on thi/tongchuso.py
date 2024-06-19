f = open("DATA.in", "r")
for line in f.readlines():
    line = line.strip()
    s = ""
    for i in line:
        if i.isdigit():
            s += i
    if s:
        tong = 0
        for i in s: tong += int(i)
        print(int(s), tong)