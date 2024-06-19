import math

class PhanSo:
    def __init__(self, tu = None, mau = None):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        c = math.gcd(self.tu, self.mau)
        self.tu = self.tu // c
        self.mau = self.mau // c
        return self.tu, self.mau
    
    def __add__(self, other):
        c = PhanSo()
        c.tu = self.tu * other.mau + self.mau * other.tu
        c.mau = self.mau * other.mau
        c.rutgon()
        return c
    
    def __str__(self):
        return (f'{self.tu}/{self.mau}')
    
list = [int(x) for x in input().split()]
a = PhanSo(list[0], list[1])
b = PhanSo(list[2], list[3])
c = a + b
print(c)