from math import ceil

class SinhVien:
    cnt = 1
    def __init__(self, ht, d1, d2, d3):
        self.ma = "SV{:02d}".format(SinhVien.cnt)
        self.ht = " ".join([i.title() for i in ht.split()])
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tb = (d1 * 3 + d2 * 3 + d3 * 2) / 8
        self.rank = 0
        SinhVien.cnt += 1

    def __str__(self):
        return "{} {} {:.2f} {}".format(self.ma, self.ht, self.tb + 0.001, self.rank)
    
hs = []
n = int(input())
for i in range(n):
    hs.append(SinhVien(input(), int(input()), int(input()), int(input())))
hs.sort(key = lambda x: -(x.tb))
hs[0].rank = 1
for i in range(1, n):
    if hs[i].tb == hs[i - 1].tb:
        hs[i].rank = hs[i - 1].rank
    else:
        hs[i].rank = i + 1
print(*hs, sep="\n")