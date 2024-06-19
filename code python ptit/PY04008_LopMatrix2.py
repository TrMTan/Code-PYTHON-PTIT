import sys
def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

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
    
    def out(self):
        for i in self.mt: print(*i)

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = next(cin), next(cin)
        mt = []
        for _ in range(n): 
            tmp = []
            for i in range(m):
                tmp.append(next(cin))
            mt.append(tmp)
        Matrix(n, m, mt).__mul__().out()
    