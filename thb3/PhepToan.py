n, k = map(int, input().split())
a = list(map(int, input().split()))
end, ok = n - 1, 0
dau  = [""] * end # dau cua cac phep toan
kytu = ["+", "-", "*"] # cac phep toan

def check():
    global ok
    bthuc = "" # bieu thuc
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

def Try(i):
    for j in kytu:
        dau[i] = j
        if i == end - 1: check()
        else: Try(i + 1)

Try(0)
if not ok: print("IMPOSSIBLE")