n, k = map(int, input().split())
a = list(map(int, input().split()))
end = n - 1
ok = 0
dau = [""] * end
kytu = ["+", "-", "*"]

def check():
    global ok
    bthuc = ""
    if a[0] < 0: bthuc += "(" + str(a[0]) + ")"
    else: bthuc += str(a[0])
    for i in range(end):
        bthuc += dau[i]
        if a[i + 1] < 0: bthuc += "(" + str(a[i + 1]) + ")"
        else: bthuc += str(a[i + 1])
    if eval(bthuc) == k:
        bthuc += "=" + str(k)
        print(bthuc)
        ok = 1
    
def Sinh(i):
    for j in kytu:
        dau[i] = j
        if i == end - 1: check()
        else: Sinh(i + 1)

Sinh(0)
if not ok: print("IMPOSSIBLE")