class MonThi:
    def __init__(self, ma, ten, ht):
        self.ma = ma
        self.ten = ten
        self.ht = ht
    
    def __str__(self):
        return "{} {} {}".format(self.ma, self.ten, self.ht)
    
a = []
for t in range(int(input())):
    a.append(MonThi(input(), input(), input()))
a.sort(key=lambda x: x.ma)
print(*a, sep="\n")
    
# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen