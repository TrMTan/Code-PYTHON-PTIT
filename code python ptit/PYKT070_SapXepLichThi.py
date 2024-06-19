# class MonThi:
#     def __init__(self, ma, ten, hinhthuc):
#         self.ma = ma
#         self.ten = ten
#         self.hinhthuc = hinhthuc

# class CaThi:
#     cnt = 1
#     def __init__(self, ngay, gio, phong):
#         self.ma = "C{:03d}".format(CaThi.cnt)
#         self.ngay = ngay
#         self.gio = gio
#         self.phong = phong
#         CaThi.cnt += 1

# class LichThi:
#     def __init__(self, cathi:CaThi, monthi: MonThi, manhom, sosv):
#         self.cathi = cathi
#         self.monthi = monthi
#         self.manhom = manhom
#         self.sosv = sosv

#     def __str__(self):
#         return "{} {} {} {} {} {}".format(self.cathi.ngay, self.cathi.gio, self.cathi.phong, self.monthi.ten, self.manhom, self.sosv)
    
# fm = open("MONTHI.in")
# fc = open("CATHI.in")
# fl = open("LICHTHI.in")

# monthi = {}
# n = int(fm.readline().strip())
# for i in range(n):
#     x = MonThi(fm.readline().strip(), fm.readline().strip(), fm.readline().strip())
#     monthi[x.ma] = x

# cathi = {}
# m = int(fc.readline().strip())
# for i in range(m):
#     x = CaThi(fc.readline().strip(), fc.readline().strip(), fc.readline().strip())
#     cathi[x.ma] = x

# lichthi = []
# k = int(fl.readline().strip())
# for i in range(k):
#     line = fl.readline().strip().split()
#     lichthi.append(LichThi(cathi[line[0]], monthi[line[1]], line[2], line[3]))

# lichthi.sort(key = lambda x: (x.cathi.ngay, x.cathi.gio, x.cathi.ma))
# for i in lichthi:
#     print(i)

class Mon:
    def __init__(self, ma, tenmon, htt):
        self.ma = ma
        self.tenmon = tenmon
        self.htt = htt

class Ca:
    cnt = 1
    def __init__(self, ngay, gio, phong):
        self.ma = "C{:03d}".format(Ca.cnt)
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        Ca.cnt += 1    
    
class Lich:
    def __init__(self, ca:Ca, mon:Mon, manhom, ssv):
        self.ca = ca
        self.mon = mon
        self.manhom = manhom
        self.ssv = ssv
        
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ca.ngay, self.ca.gio, self.ca.phong, self.mon.tenmon, self.manhom, self.ssv)
        
f1 = open("MONTHI.in", "r")
f2 = open("CATHI.in", "r")
f3 = open("LICHTHI.in", "r")

mon = {}
for i in range(int(f1.readline().strip())):
    x = Mon(f1.readline().strip(), f1.readline().strip(), f1.readline().strip())
    mon[x.ma] = x

ca = {}
for i in range(int(f2.readline().strip())):
    x = Ca(f2.readline().strip(), f2.readline().strip(), f2.readline().strip())
    ca[x.ma] = x
    
lich = []
for i in range(int(f3.readline().strip())):
    s = f3.readline().strip().split()
    lich.append(Lich(ca[s[0]], mon[s[1]], s[2], s[3]))
lich.sort(key = lambda x : (x.ca.ngay, x.ca.gio, x.ca.ma))
print(*lich, sep = "\n")