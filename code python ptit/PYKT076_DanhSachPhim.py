# from datetime import datetime
# class TheLoaiPhim:
#     cnt = 1
#     def __init__(self, tl):
#         self.ma = "TL{:03}".format(TheLoaiPhim.cnt)
#         self.tl = tl
#         TheLoaiPhim.cnt += 1
    
#     def getMa(self):
#         return self.ma
    
#     def getTL(self):
#         return self.tl
    
# class Phim:
#     cnt = 1
#     def __init__(self, tl, date, tapso, sotap):
#         self.ma = "P{:03}".format(Phim.cnt)
#         self.tl = tl
#         self.date = datetime.strptime(date, '%d/%m/%Y')
#         self.strdate = date
#         self.tapso = tapso
#         self.sotap = sotap
#         self.theLoai = ""
#         Phim.cnt += 1
    
#     def setTheLoai(self, theLoai):
#         self.theLoai = theLoai

#     def __str__(self):
#         return "{} {} {} {} {}".format(self.ma, self.theLoai, self.strdate, self.tapso, self.sotap)
    
# n, m = map(int, input().split())
# tlp = []
# for i in range(n):
#     tlp.append(TheLoaiPhim(input()))

# p = []
# for i in range(m):
#     a = Phim(input(), input(), input(), input())
#     p.append(a)

# for i in tlp:
#     for j in p:
#         if i.getMa() == j.tl:
#             j.setTheLoai(i.getTL())

# p = sorted(p, key=lambda x: x.date)
# print(*p, sep='\n')

class TheLoai:
    cnt = 1
    def __init__(self, tl):
        self.ma = "TL{:03}".format(TheLoai.cnt)
        self.tl = tl
        TheLoai.cnt += 1
    
class Phim:
    cnt = 1
    def __init__(self, tl:TheLoai, ngay, tenphim, sotap):
        self.ma = "P{:03}".format(Phim.cnt)
        self.tl = tl 
        self.ngay = ngay
        self.tenphim = tenphim
        self.sotap = sotap
        Phim.cnt += 1
    def __str__(self):
        return "{} {} {} {} {}".format(self.ma, self.tl.tl, self.ngay, self.tenphim, self.sotap)

n, m = map(int, input().split())
tl = {}
for i in range(n):
    x = TheLoai(input())
    tl[x.ma] = x

p = []
for i in range(m):
    x = Phim(tl[input()], input(), input(), input())  
    p.append(x)

p.sort(key = lambda x: x.ngay, reverse=True)
print(*p, sep = '\n')