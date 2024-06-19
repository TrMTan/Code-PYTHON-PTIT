class SinhVien:
    def __init__(self, msv, ht, lop):
        self.msv = msv
        self.ht = ht
        self.lop = lop
        self.cc = 10
    
    def getMa(self):
        return self.msv
    
    def tinhdiem(self, dd):
        for i in dd:
            if i == 'm': self.cc -= 1
            elif i == 'v': self.cc -= 2
        if self.cc < 0: self.cc = 0
    
    def __str__(self):
        res = self.msv + " " + self.ht + " " + self.lop + " " + str(self.cc)
        if self.cc == 0: res += " KDDK"
        return res

n = int(input())
sv = []
for i in range(n):
    s = SinhVien(input(), input(), input())
    sv.append(s)
for i in range(n):
    a = input().split()
    for j in sv:
        if j.getMa() == a[0]:
            j.tinhdiem(a[1])
for i in sv:
    print(i)

# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm