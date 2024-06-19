class SinhVien:
    def __init__(self, msv, ht, sdt, email):
        self.msv = msv
        self.ht = ht
        self.sdt = sdt
        self.email = email
        a = ht.split()
        self.ho = a[0]
        self.ten = a[-1]
        self.tenDem = " ".join(a[1:-1])
    def __str__(self):
        return "{} {} {} {}".format(self.msv, self.ht, self.sdt, self.email)
    
f = open("SINHVIEN.in", "r")
sv = []
for i in range(int(f.readline().strip())):
    sv.append(SinhVien(f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()))

sv.sort(key = lambda x : (x.ten, x.ho, x.tenDem, x.msv), reverse=False)
print(*sv, sep = "\n")