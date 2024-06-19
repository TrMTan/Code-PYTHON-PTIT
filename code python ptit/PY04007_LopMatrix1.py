class Matrix:

    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
    
    def __mul__(self):
        res = []
        for i in range(self.n):
            res += [[0] * self.n]
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j] += self.mt[i][k] * self.mt[j][k]
        return Matrix(self.m, self.n, res)
    
    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''

for i in range(int(input())):
    n, m = [int(x) for x in input().split()]
    mt = []
    for i in range(n):
        mt.append([int(x) for x in input().split()])
    a = Matrix(n, m, mt)
    print(a.__mul__())