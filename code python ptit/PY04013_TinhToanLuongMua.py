from datetime import datetime
class Mua:
    cnt = 1
    def __init__(self, ten, bd, kt, lm):
        self.ma = "T{:02d}".format(Mua.cnt)
        self.ten = ten
        self.time = (datetime.strptime(kt, '%H:%M') - datetime.strptime(bd, '%H:%M')).seconds / 3600
        self.lm = lm
        Mua.cnt += 1
    def __str__(self):
        return "{} {} {:.2f}".format(self.ma, self.ten, self.lm / self.time)
a = []
def tinhMua(data):
    for i in a:
        if i.ten == data.ten:
            i.time += data.time
            i.lm += data.lm
            return
    a.append(data)
for i in range(int(input())):
    s = (Mua(input(), input(), input(), int(input())))
    tinhMua(s)

print(*a, sep = "\n")

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35