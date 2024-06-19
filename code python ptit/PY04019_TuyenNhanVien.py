class NhanVien:
    cnt = 1
    def __init__(self, ht, lt, th):
        self.manv = "TS{:02d}".format(NhanVien.cnt) if NhanVien.cnt < 10 else "TS{:03d}".format(NhanVien.cnt)
        self.ht = ht
        self.lt = lt
        self.th = th

        self.lt /= 10 if self.lt > 10 else 1
        self.th /= 10 if self.th > 10 else 1

        self.tong = (self.lt + self.th) / 2

        if self.tong >= 9.5:
            self.kq = "XUAT SAC"
        elif self.tong >= 8:
            self.kq = "DAT"
        elif self.tong >= 5:
            self.kq = "CAN NHAC"
        else:
            self.kq = "TRUOT"                    
        NhanVien.cnt += 1

    def __str__(self):
        return "{} {} {} {}".format(self.manv, self.ht, ("%.2f" % self.tong), self.kq)    

    def __lt__(self, other):
        return self.tong > other.tong
    
a = []
for i in range(int(input())):
    s = NhanVien(input(), float(input()), float(input()))
    a.append(s)    
a.sort()
for i in a:
    print(i)

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56