class MatHang:
    def __init__(self, ma, ten, sl, dongia, chietkhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tong = self.dongia * self.sl - self.chietkhau
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.sl, self.dongia, self.chietkhau, self.tong)
    
    def __lt__(self, other):
        return self.tong > other.tong
a = []
for i in range(int(input())):
    s = MatHang(input(), input(), int(input()), int(input()), int(input()))
    a.append(s)
a.sort()
for i in a:
    print(i)

# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000