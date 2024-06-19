class Phong:
    def __init__(self, maP, tenP):
        self.maP = maP
        self.tenP = tenP

    def getTenP(self):
        return self.tenP
    
    def getMaP(self):
        return self.maP

class NhanVien:
    def __init__(self, maNV, ht, lcb, nc):
        self.maNV = maNV
        self.ht = ht
        self.lcb = lcb
        self.nc = nc
        self.tenP = ""

    def cal(self):
        nhom = self.maNV[0]
        nam = int(self.maNV[1:3])
        self.hs = 1
        if nhom == 'A':
            if nam in range(1, 4): self.he_so_luong = 10
            if nam in range(4, 9): self.he_so_luong = 12
            if nam in range(9, 16): self.he_so_luong = 14
            if nam >= 16: self.he_so_luong = 20
        elif nhom == 'B':
            if nam in range(1, 4): self.he_so_luong = 10
            if nam in range(4, 9): self.he_so_luong = 11
            if nam in range(9, 16): self.he_so_luong = 13
            if nam >= 16: self.he_so_luong = 16
        elif nhom == 'C':
            if nam in range(1, 4): self.he_so_luong = 9
            if nam in range(4, 9): self.he_so_luong = 10
            if nam in range(9, 16): self.he_so_luong = 12
            if nam >= 16: self.he_so_luong = 14
        elif nhom == 'D':
            if nam in range(1, 4): self.he_so_luong = 8
            if nam in range(4, 9): self.he_so_luong = 9
            if nam in range(9, 16): self.he_so_luong = 11
            if nam >= 16: self.he_so_luong = 13
        return self.he_so_luong * self.lcb * self.nc * 1000

    def getPhong(self):
        return self.maNV[3:]
    
    def setPhong(self, tenP):
        self.tenP = tenP

    def __str__(self):
        return self.maNV + ' ' + self.ht + ' ' + self.tenP + ' ' + str(self.cal())
               
phong = []
for i in range(int(input())):
    a = input()
    maP = a[:2]
    tenP = a[3:]
    phong.append(Phong(maP, tenP))

nhanvien = []
for i in range(int(input())):
    nhanvien.append(NhanVien(input(), input(), int(input()), int(input())))

for p in phong:
    for nv in nhanvien:
        if p.getMaP() == nv.getPhong():
            nv.setPhong(p.getTenP())
print(*nhanvien, sep='\n')


