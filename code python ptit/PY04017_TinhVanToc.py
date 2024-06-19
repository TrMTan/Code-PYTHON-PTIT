class TayDua:
    def __init__(self, ht, dv, time):
        self.ht = ht
        self.dv = dv
        self.time = time
        a = ""
        for i in self.ht.split():
            a += i[0]
        b = ""
        for i in self.dv.split():
            b += i[0]
        self.ma = b + a
        gio = int(self.time.split(":")[0])
        phut = int(self.time.split(":")[1])
        self.tonggio = (gio - 6) + (phut / 60)
        self.vt = 120 / self.tonggio

    def __str__(self):
        return "{} {} {} {} Km/h".format(self.ma, self.ht, self.dv, round(self.vt))

td = []
for i in range(int(input())):
    ht = input()
    dv = input()
    time = input()
    td.append(TayDua(ht, dv, time))

td = sorted(td, key = lambda x: -x.vt)
for i in td:
    print(i)