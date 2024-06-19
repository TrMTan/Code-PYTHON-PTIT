from datetime import datetime

class SinhVien:
    def __init__(self, ht, bd, kt):
        self.ht = ht
        self.bd = bd
        self.kt = kt
        self.time = (datetime.strptime(kt,'%d/%m/%Y %H:%M:%S') - datetime.strptime(bd, '%d/%m/%Y %H:%M:%S')).seconds // 60 + (datetime.strptime(kt, '%d/%m/%Y %H:%M:%S') - datetime.strptime(bd, '%d/%m/%Y %H:%M:%S')).days * 24 * 60
    def __str__(self):
        return "{} {}".format(self.ht, self.time)

f = open("ONLINE.in", "r")
a = []
for i in range(int(f.readline().strip())):
    a.append(SinhVien(f.readline().strip(), f.readline().strip(), f.readline().strip()))
a.sort(key = lambda x: (x.time, x.ht), reverse = True)
print(*a, sep = "\n")

# 3
# Do Viet Anh
# 11/12/2021 16:35:00
# 11/12/2021 17:35:00
# Le Tuan Anh
# 11/12/2021 16:45:00
# 11/12/2021 18:15:00
# Nguyen Tuan Anh
# 11/12/2021 17:00:00
# 11/12/2021 19:15:00