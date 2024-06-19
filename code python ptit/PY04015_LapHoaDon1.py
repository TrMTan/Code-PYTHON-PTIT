class HoaDon:
    def __init__(self, ma, ht, cu, moi):
        self.ma = ma
        self.ht = ht
        self.moi = moi
        self.cu = cu
        self.tong = self.moi - self.cu
        if self.tong <= 50:
            self.tong *= 100
            self.tong += self.tong * 0.02
        elif self.tong <= 100:
            self.tong = 50 * 100 + (self.tong - 50) * 150
            self.tong += self.tong * 0.03
        else:
            self.tong = 50 * 100 + 50 * 150 + (self.tong - 100) * 200
            self.tong += self.tong * 0.05

    def __str__(self):
        return "{} {} {}".format(self.ma, self.ht, round(self.tong))

a = []
for i in range(int(input())):
    ma = "KH{:02d}".format(i + 1)
    s = HoaDon(ma, input(), int(input()), int(input()))
    a.append(s)
a.sort(key=lambda x: -x.tong)
for i in a:
    print(i)

# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612