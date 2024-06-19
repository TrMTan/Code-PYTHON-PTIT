class MonHoc:
    def __init__(self, mamon, ten, tc):
        self.mamon = mamon
        self.ten = ten
        self.tc = tc

class LichGD: 
    cnt = 1
    def __init__(self, mh:MonHoc, thu, kip, htgv, phong):
        self.maNhom = "HP{:03d}".format(LichGD.cnt)
        self.mh = mh
        self.thu = thu
        self.kip = kip
        self.htgv = htgv
        self.phong = phong
        LichGD.cnt += 1
    
    def __str__(self):
        return "{} {} {} {} {}".format(self.maNhom, self.thu, self.kip, self.htgv, self.phong)
f1 = open("MONHOC.in", "r")
f2 = open("LICHGD.in", "r")
mh = {}
for i in range(int(f1.readline().strip())):
    x = MonHoc(f1.readline().strip(), f1.readline().strip(), f1.readline().strip())
    mh[x.mamon] = x
lich = []
for i in range(int(f2.readline().strip())):
    lich.append(LichGD(mh[f2.readline().strip()], f2.readline().strip(), f2.readline().strip(), f2.readline().strip(), f2.readline().strip()))
lich.sort(key = lambda x : (x.thu))
mamon = f2.readline().strip()
for i in lich:
    if i.mh.mamon == mamon:
        ten = i.mh.ten
print("LICH DANG DAY MON " + ten + ":")
for i in lich:
    if i.mh.mamon == mamon:
        print(i)

# 2
# INT1155
# Tin hoc co so 2
# 2
# INT13162
# Lap trinh voi Python
# 3
# 4
# INT13162
# 5
# 1
# Nguyen Hoang Anh
# 102-A2
# INT1155
# 3
# 1
# Nguyen Dinh Hien
# 201A-A3
# INT1155
# 4
# 1
# Nguyen Quy Sy
# 201A-A3
# INT1155
# 5
# 1
# Tran Quy Nam
# 201A-A3
# INT1155
