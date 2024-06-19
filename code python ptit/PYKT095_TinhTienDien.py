class TinhTien: 
    cnt = 1
    def __init__(self, ht, loai, sd, sc):
        self.ma = "KH{:02d}".format(TinhTien.cnt)
        self.ht = " ".join([i.title() for i in ht.split()])
        self.loai = loai
        self.sd = sd
        self.sc = sc
        self.sodien = self.sc - self.sd
        self.dinhmuc = 0
        if self.loai == "A":
            self.dinhmuc = 100
        elif self.loai == "B":
            self.dinhmuc = 500
        else:
            self.dinhmuc = 200
        self.tiendm = 0
        self.tienvdm = 0
        if self.sodien < self.dinhmuc:
            self.tiendm = self.sodien * 450
            self.tienvdm = 0
        else:
            self.tiendm = self.dinhmuc * 450
            self.tienvdm = (self.sodien - self.dinhmuc) * 1000
        self.thue = self.tienvdm * 5 / 100
        self.tong = self.tiendm + self.tienvdm + self.thue
        TinhTien.cnt += 1
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ht, self.tiendm, self.tienvdm, int(self.thue), int(self.tong))

a = []
for i in range(int(input())):
    ht = input()
    s = input()
    loai, sd, sc = s.split()
    a.append(TinhTien(ht, loai, int(sd), int(sc)))
a.sort(key = lambda x: -x.tong)
for i in a:
    print(i)