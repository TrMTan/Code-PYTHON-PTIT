class SinhVien:
    def __init__(self, msv, ht, sdt, email):
        self.msv = msv
        self.ht = ht
        self.sdt = sdt
        self.email = email

class DeTai:
    cnt = 1
    def __init__(self, tengv, tendt):
        self.ma = "DT{:03d}".format(DeTai.cnt)
        self.tengv = tengv
        self.tendt = tendt
        DeTai.cnt += 1
        
class HoiDong   :
    def __init__(self, sv: SinhVien, dt: DeTai, mahd):
        self.sv = sv
        self.dt = dt
        self.mahd = mahd
    def __str__(self):
        return "{} {} {} {}".format(self.sv.msv, self.sv.ht, self.dt.tendt, self.dt.tengv)
    
f1 = open("SINHVIEN.in", "r")
f2 = open("DETAI.in", "r")
f3 = open("HOIDONG.in", "r")

sv = {}
for i in range(int(f1.readline().strip())):
    x = SinhVien(f1.readline().strip(), f1.readline().strip(), f1.readline().strip(), f1.readline().strip())
    sv[x.msv] = x

dt = {}
for i in range(int(f2.readline().strip())):
    x = DeTai(f2.readline().strip(), f2.readline().strip())
    dt[x.ma] = x

hd = []
for i in range(int(f3.readline().strip())):
    s = f3.readline().strip().split()
    hd.append(HoiDong(sv[s[0]], dt[s[1]], s[2]))

hd.sort(key = lambda x: (x.sv.msv), reverse=True)
for i in hd:
    print("DANH SACH HOI DONG " + i.mahd[-1])
    print(i)