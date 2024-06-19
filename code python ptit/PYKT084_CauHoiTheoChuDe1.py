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


# 9
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?
 
# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?