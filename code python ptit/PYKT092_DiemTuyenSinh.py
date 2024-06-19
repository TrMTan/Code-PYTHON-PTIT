class ThiSinh:
    cnt = 1
    def __init__(self, ht, diem, dt, kv):
        self.ma = "TS{:02d}".format(ThiSinh.cnt)
        self.ht = ht
        self.diem = diem
        self.dt = dt
        self.kv = kv

        ten = ht.split()
        self.ht = ""
        for i in ten: self.ht += i.title() + " "

        if dt != "Kinh": self.diem += 1.5
        if kv == 1: self.diem += 1.5
        elif kv == 2: self.diem += 1

        if self.diem >= 20.5: self.kq = "Do"
        else: self.kq = "Truot"

        ThiSinh.cnt += 1
    
    def __str__(self):
        return "{} {}{} {}".format(self.ma, self.ht, ("%.1f" % self.diem), self.kq)
    
    def __lt__(self, other):
        if self.diem != other.diem: 
            return self.diem > other.diem
        return self.ma < other.ma
    
a = []
for i in range(int(input())):
    a.append(ThiSinh(input(), float(input()), input(), int(input())))
a.sort()
for i in a: 
    print(i)

# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3