class ThiSinh:
    cnt = 1
    def __init__(self, ht, maxt, dt, dcm):
        self.ma = "GV{:02d}".format(ThiSinh.cnt)
        self.ht = ht
        self.maxt = maxt
        self.dt = dt
        self.dcm = dcm

        if self.maxt[0] == "A": self.mon = "TOAN"
        elif self.maxt[0] == "B": self.mon = "LY"
        elif self.maxt[0] == "C": self.mon = "HOA"

        if self.maxt[1] == "1": self.dut = 2.0
        elif self.maxt[1] == "2": self.dut = 1.5
        elif self.maxt[1] == "3": self.dut = 1.0
        else: self.dut = 0.0

        self.tong = self.dt * 2 + self.dcm + self.dut

        if self.tong >= 18:
            self.kq = "TRUNG TUYEN"
        else:
            self.kq = "LOAI"

        ThiSinh.cnt += 1

    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.ma, self.ht, self.mon, self.tong, self.kq)

    def __lt__(self, other):
        return self.tong > other.tong
    
a = []
for i in range(int(input())):
    a.append(ThiSinh(input(), input(), float(input()), float(input())))
a.sort()
for i in a:
    print(i)

# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0