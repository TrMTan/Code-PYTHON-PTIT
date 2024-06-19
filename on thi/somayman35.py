n = input()
cnt3 = 0
cnt5 = 0
for i in n: 
    if i == "3": cnt3 += 1
    if i == "5": cnt5 += 1
if cnt3 + cnt5 == 3 or cnt3 + cnt5 == 5: print("YES")
else: print("NO")