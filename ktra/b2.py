from datetime import datetime

class TheLoai:
    def __init__(self, i, ten):
        self.ma = f'TL{str(i).zfill(3)}'
        self.ten = ten

class Phim(TheLoai):
    def __init__(self, i, maTL, date, tapso, sotap):
        self.ma = f'P{str(i).zfill(3)}'
        self.maTL = maTL
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.strdate = date
        self.tapso = tapso
        self.tap = sotap
    def __str__(self):
        return self.ma + ' ' + self.maTL + ' ' + self.strdate + ' ' + self.tapso + ' ' +self.tap
    
n, m = map(int, input().split())

tl, p = {}, []

for i in range(n):
    s = TheLoai(i + 1, input())
    tl[s.ma] = s.ten

for i in range(m):
    a = Phim(i + 1, tl[input()], input(), input(), input())
    p.append(a)

p = sorted(p, key=lambda x: x.date)
for i in p: 
    print(i)

# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5
