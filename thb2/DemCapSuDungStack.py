from collections import deque

n = int(input())
s = deque()
s.append([int(input()), 1]) # thêm phần tử đầu tiên vào stack, số lần xuất hiện của phần tử đó là 1
kq = 0
for i in range(1, n):
    x = int(input())
    while len(s) > 0:
        if x < s[-1][0]: # nếu x nhỏ hơn phần tử cuối cùng của stack
            kq += 1
            s.append([x, 1]) # thêm x vào stack, số lần xuất hiện của x là 1
            break
        else:
            tmp = s.pop() # lấy phần tử cuối cùng của stack
            kq += tmp[1] # cập nhật kết quả
            if tmp[0] == x: # nếu phần tử cuối cùng của stack bằng x
                kq += 1 if len(s) > 0 else 0 # cập nhật kết quả
                s.append([x, tmp[1] + 1]) # thêm x vào stack, số lần xuất hiện của x tăng thêm 1
                break
    if len(s) == 0: s.append([x, 1]) # nếu stack rỗng, thêm x vào stack, số lần xuất hiện của x là 1
print(kq)

        