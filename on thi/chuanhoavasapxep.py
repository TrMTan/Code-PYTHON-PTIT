class GiangVien:
    def __init__(self, ht):
        self.ht = " ".join([i.title() for i in ht.split()])
        a = ht.lower().split()
        self.ho = a[0]
        self.ten = a[-1]
        self.dem = " ".join(a[1:-1])
    def __str__(self):
        return "{}".format(self.ht)

f = open("SINHVIEN.in", "r")
names = f.readlines()

a = []
for i in names:
    a.append(GiangVien(i.strip()))
a.sort(key = lambda x : (x.ten, x.ho, x.dem))
for i in a:
    print(i)    