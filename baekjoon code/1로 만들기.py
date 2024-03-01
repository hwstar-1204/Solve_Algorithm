"""
x가 1이 되는 경우 
= 입력값에서 3으로 나누거나 2로 나누거나 + 입력값-1에서 3으로 나누거나 2로 나누거나 
"""

x = int(input())
cnt_list = [0]*(x+1)
# 0 0 1 2 
for i in range(2,x+1):
    cnt_list[i] = cnt_list[i-1] + 1
    if i % 3 == 0:
        cnt_list[i] = min(cnt_list[i],cnt_list[i//3]+1)
    if i % 2 == 0:
        cnt_list[i] = min(cnt_list[i],cnt_list[i//2]+1)
print(cnt_list[x])


# def DivX(x,cnt):
#     if x == 1:
#         return cnt  

#     if x % 3 == 0:
#         return DivX(x//3,cnt+1)
#     elif x % 2 == 0:
#         return DivX(x//2,cnt+1)
#     else:
#         return DivX(x-1,cnt+1)

# a = DivX(x,0)
# b = DivX(x-1,1)

# result = a if a < b else b
# print(result)