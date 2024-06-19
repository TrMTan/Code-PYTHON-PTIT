class CaThi:
    cnt = 1
    def __init__(self, ngay, gio, phong):
        self.ma = "C{:03d}".format(CaThi.cnt)
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        CaThi.cnt += 1
    def __str__(self):
        return "{} {} {} {}".format(self.ma, self.ngay, self.gio, self.phong)

a = []
f = open("CATHI.in", "r")
for i in range(int(f.readline())):
    a.append(CaThi(f.readline().strip(), f.readline().strip(), f.readline().strip()))

a.sort(key = lambda x: (x.ngay, x.gio, x.ma))
for i in a:
    print(i)