# class Mon:
#     def __init__(self, ma, ten):
#         self.ma = ma
#         self.ten = ten

#     def getMa(self):
#         return self.ma
    
#     def getTen(self):
#         return self.ten
        
# class LichThi:
#     cnt = 1
#     def __init__(self, mamon, ngay, gio, nhom):
#         self.ma = "T{:03d}".format(LichThi.cnt)
#         self.mamon = mamon
#         self.ngay = ngay
#         self.gio = gio
#         self.nhom = nhom
#         self.ngaythi = ngay[0:2]
#         self.thangthi = ngay[3:5]
#         self.namthi = ngay[6:10]
#         self.giothi = gio[0:2]
#         self.phutthi = gio[3:5]
#         self.tenmon = ""
#         LichThi.cnt += 1
    
#     def getMa(self):
#         return self.ma
#     def setTenMon(self, ten):
#         self.tenmon = ten
    
#     def __str__(self):
#         return "{} {} {} {} {} {}".format(self.ma, self.mamon, self.tenmon, self.ngay, self.gio, self.nhom)
    
# n, m = map(int, input().split())
# monhoc = []    
# for i in range(n):
#     ma = input()
#     mon = input()
#     monhoc.append(Mon(ma, mon))
# lichthi = []
# for i in range(m):
#     s = input().split()
#     lichthi.append(LichThi(s[0], s[1], s[2], s[3]))

# for i in monhoc:
#     for j in lichthi:
#         if i.getMa() == j.mamon:
#             j.setTenMon(i.getTen())

# lichthi.sort(key = lambda x : (x.namthi, x.thangthi, x.ngaythi, x.giothi, x.phutthi, x.mamon))
# for i in lichthi:
#     print(i)

class MonThi:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class LichThi:
    cnt = 1
    def __init__(self, mt:MonThi, ngay, gio, nhom):
        self.ma = "T{:03d}".format(LichThi.cnt)
        self.mt = mt
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom
        self.ngaythi = ngay[0:2]
        self.thangthi = ngay[3:5]
        self.namthi = ngay[6:10]
        self.giothi = gio[0:2]
        self.phutthi = gio[3:5]
        LichThi.cnt += 1
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.mt.ma, self.mt.ten, self.ngay, self.gio, self.nhom)
    
n, m = map(int, input().split())
monthi = {}
for i in range(n):
    x = MonThi(input(), input())
    monthi[x.ma] = x

lichthi = []
for i in range(m):
    s = input().split()
    lichthi.append(LichThi(monthi[s[0]], s[1], s[2], s[3]))

lichthi.sort(key = lambda x: (x.namthi, x.thangthi, x.ngaythi, x.giothi, x.phutthi, x.mt.ma))
print(*lichthi, sep = '\n')
    