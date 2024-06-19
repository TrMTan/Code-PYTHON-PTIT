from datetime import datetime

class Game:
    def __init__(self, ma, ht, bd, kt):
        self.ma = ma
        self.ht = ht
        self.thoigian = (datetime.strptime(kt, '%H:%M') - datetime.strptime(bd, '%H:%M')).seconds
    def __str__(self):
        return "{} {} {} gio {} phut".format(self.ma, self.ht, self.thoigian // 3600, self.thoigian // 60 % 60)

a = []
for i in range(int(input())):
    a.append(Game(input(), input(), input(), input()))
a.sort(key = lambda x : -x.thoigian)
print(*a, sep = "\n")

# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00