n = int(input())
data = []    
for i in range(n):
    a = input()
    if a == "":
        print(f"{data[0]}: {len(data) - 1}")
        data.clear()
    else: 
        data.append(a)
print(f"{data[0]}: {len(data) - 1}")