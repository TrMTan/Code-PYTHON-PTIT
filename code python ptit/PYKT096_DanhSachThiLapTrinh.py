# class Team: 
#     cnt = 1
#     def __init__(self, ten, truong):
#         self.ma = "Team{:02}".format(Team.cnt)
#         self.ten = ten
#         self.truong = truong
#         Team.cnt += 1

#     def getMa(self):
#         return self.ma
    
#     def getTen(self):
#         return self.ten
    
#     def getTruong(self):
#         return self.truong
    
# class ThiSinh:
#     cnt = 1
#     def __init__(self, ht, team):    
#         self.ma = "C{:03}".format(ThiSinh.cnt)
#         self.ht = ht
#         self.team = team
#         ThiSinh.cnt += 1

#     def getTeam(self):
#         return self.team
        
#     def __str__(self, tenTeam, tenTruong):
#         return "{} {} {} {}".format(self.ma, self.ht, tenTeam, tenTruong)
    
#     def __lt__(self, other):
#         return self.ht < other.ht
    
# n = int(input())    
# team = []
# for i in range(n):
#     t = Team(input(), input())
#     team.append(t)

# m = int(input())
# ts = []
# for i in range(m):
#     s = ThiSinh(input(), input())
#     ts.append(s)

# ts.sort()
# for i in ts:
#     for j in team:
#         if i.getTeam() == j.getMa():
#             print(i.__str__(j.getTen(), j.getTruong()))

class Team:
    cnt = 1
    def __init__(self, ten, truong):
        self.ma = "Team{:02d}".format(Team.cnt)
        self.ten = ten
        self.truong = truong
        Team.cnt += 1
class ThiSinh:
    cnt = 1
    def __init__(self, ht, team:Team):
        self.ma = "C{:03d}".format(ThiSinh.cnt)
        self.ht = ht
        self.team = team
        ThiSinh.cnt += 1
        
    def __str__(self):
        return "{} {} {} {}".format(self.ma, self.ht, self.team.ten, self.team.truong)
        
team = {}
for i in range(int(input())):
    x = Team(input(), input())
    team[x.ma] = x
thisinh = []
for i in range(int(input())):
    thisinh.append(ThiSinh(input(), team[input()]))
thisinh.sort(key = lambda x : x.ht)
print(*thisinh, sep = "\n")