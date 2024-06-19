class SinhVien:
    cnt = 1
    def __init__(self, ten, diem, dt, kv):
        self.id = "TS{:02d}".format(SinhVien.cnt)
        self.ten = ten
        self.diem = diem
        self.dt = dt
        self.kv = kv
        if dt != "Kinh":
            self.diem += 1.5
        if kv == 1:
            self.diem += 1.5
        elif kv == 2:
            self.diem += 1
        if self.diem >= 20.5:
            self.kq = "Do"
        else:
            self.kq = "Truot"
        SinhVien.cnt += 1

    def chuanHoa(self):
        self.ten = self.ten.title().split()
        return " ".join(self.ten)
    
    def __lt__(self, other):
        if self.diem != other.diem:
            return self.diem > other.diem
        return self.id < other.id

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.chuanHoa(), self.diem, self.kq)
    
sv = []
for i in range(int(input())):
    sv.append(SinhVien(input(), float(input()), input(), int(input())))
sv.sort()
print(*sv, sep="\n")
