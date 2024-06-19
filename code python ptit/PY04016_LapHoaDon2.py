from datetime import datetime

class KhachHang:
    cnt = 1
    def __init__(self, ht, sp, nn, nt, dv):
        self.ma = "KH{:02d}".format(KhachHang.cnt)
        self.ht = ht
        self.sp = sp
        self.nn = nn
        self.nt = nt
        d0 = datetime.strptime(nn, '%d/%m/%Y')
        d1 = datetime.strptime(nt, '%d/%m/%Y')
        d = d1 - d0
        self.ngay = d.days + 1
        self.dv = dv
        self.tongtien = 0
        self.gia = 0
        if self.sp[0] == '1':
            self.gia = 25
        elif self.sp[0] == '2':
            self.gia = 34
        elif self.sp[0] == '3':
            self.gia = 50
        else: self.gia = 80  
        KhachHang.cnt += 1
        self.tongtien = self.ngay * self.gia + self.dv

    def __str__(self):
        return "{} {} {} {} {}".format(self.ma, self.ht, self.sp, self.ngay, self.tongtien)
    
kh = []
for i in range(int(input())):
    ht = input().strip()
    sp = input().strip()
    nn = input().strip()
    nt = input().strip()
    dv = int(input())
    kh.append(KhachHang(ht, sp, nn, nt, dv))

kh = sorted(kh, key=lambda x: (-x.tongtien))
for i in kh:
    print(i)

        