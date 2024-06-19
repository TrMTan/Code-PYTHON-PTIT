class MonHoc:
    def __init__(self, mamon, ten, tc, lt, th):
        self.mamon = mamon
        self.ten = ten
        self.tc = tc
        self.lt = lt
        self.th = th
    
    def __str__(self):
        return "{} {} {} {} {}".format(self.mamon, self.ten, self.tc, self.lt, self.th)

f = open("MONHOC.in", "r")
mh = []
for i in range(int(f.readline().strip())):
    mh.append(MonHoc(f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()))

mh.sort(key = lambda x : (x.mamon))
print(*mh, sep = "\n")

