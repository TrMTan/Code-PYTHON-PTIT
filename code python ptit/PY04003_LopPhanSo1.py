import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        c = math.gcd(self.tu, self.mau)
        self.tu = self.tu // c
        self.mau = self.mau // c
    
    def __str__(self):
        self.rutgon()
        print(f'{self.tu}/{self.mau}')
    
tu, mau = [int(x) for x in input().split()]
a = PhanSo(tu, mau)
a.__str__()