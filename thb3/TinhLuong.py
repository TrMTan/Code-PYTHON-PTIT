class Phong:
    def __init__(self, maP, tenP):
        self.maP = maP
        self.tenP = tenP

    def getMaP(self):
        return self.maP
    
    def getTenP(self):
        return self.tenP
    
class NhanVien:
    def __init__(self, maNV, tenNV, luongcb, nc):
        self.maNV = maNV
        self.tenNV = tenNV
        self.luongcb = luongcb
        self.nc = nc
        self.tenP = ""

    def tinhLuong(self):
        nhom = self.maNV[0]
        nam = int(self.maNV[1:3])
        self.hs = 1
        if nhom == 'A':
            if nam in range(1, 4): self.hs = 10
            elif nam in range(4, 9): self.hs = 12
            elif nam in range(9, 16): self.hs = 14
            else: self.hs = 20
        elif nhom == 'B':
            if nam in range(1, 4): self.hs = 10
            elif nam in range(4, 9): self.hs = 11
            elif nam in range(9, 16): self.hs = 13
            else: self.hs = 16
        elif nhom == 'C':
            if nam in range(1, 4): self.hs = 9
            elif nam in range(4, 9): self.hs = 10
            elif nam in range(9, 16): self.hs = 12
            else: self.hs = 14
        else:
            if nam in range(1, 4): self.hs = 8
            elif nam in range(4, 9): self.hs = 9
            elif nam in range(9, 16): self.hs = 11
            else: self.hs = 13
        return self.hs * 1000 * self.nc * self.luongcb
        
    def getMaPhong(self):
        return self.maNV[3:]
        
    def setTenPhong(self, tenP):
        self.tenP = tenP
        
    def __str__(self):
        return "{} {} {} {}".format(self.maNV, self.tenNV, self.tenP, self.tinhLuong())

phong = []
for i in range(int(input())):
    a = input()
    maP = a[:2]
    tenP = a[3:]
    phong.append(Phong(maP, tenP))

nhanvien = []
for i in range(int(input())):
    maNV = input()
    tenNV = input()
    luongcb = int(input())
    nc = int(input())
    nhanvien.append(NhanVien(maNV, tenNV, luongcb, nc))

for p in phong:
    for nv in nhanvien:
        if p.getMaP() == nv.getMaPhong():
            nv.setTenPhong(p.getTenP())
print(*nhanvien, sep="\n")