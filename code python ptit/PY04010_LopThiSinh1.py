class ThiSinh:
    def __init__(self, ht, ns, d):
        self.ht = ht
        self.ns = ns
        self.d = sum(d)

    def __str__(self):
        return f'{self.ht} {self.ns} {self.d}'

ht = input()
ns = input()
d = [float(input()), float(input()), float(input())]
print(ThiSinh(ht, ns, d))
