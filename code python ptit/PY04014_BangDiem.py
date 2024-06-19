class Student:
    cnt = 1
    def __init__(self, ht, diem):
        self.id = "HS{:02}".format(Student.cnt)
        self.ht = ht
        self.diem = diem
        self.diemTB = sum(diem) + diem[0] + diem[1]
        self.diemTB = round(((self.diemTB / 12.0) * 10) / 10.0, 1)
        
        if self.diemTB >= 9.0:
            self.xeploai = "XUAT SAC"
        elif self.diemTB >= 8.0:
            self.xeploai = "GIOI"
        elif self.diemTB >= 7.0:
            self.xeploai = "KHA"
        elif self.diemTB >= 5.0:
            self.xeploai = "TB"
        else:
            self.xeploai = "YEU"
        Student.cnt += 1
    
    def __str__(self):
        return "{} {} {} {}".format(self.id, self.ht, self.diemTB, self.xeploai)
    
    def __lt__(self, other):
        if self.diemTB != other.diemTB:
            return self.diemTB > other.diemTB
        return self.id < other.id
    
a = []    
for i in range(int(input())):
    s = Student(input(), [float(x) for x in input().split()])
    a.append(s)
print(*sorted(a), sep = "\n")

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0