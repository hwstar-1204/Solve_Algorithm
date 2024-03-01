#구간의 합 

mylist = list(map(int,input().split()))
prefix_list = []
temp = 0

for n in mylist:
    temp += n
    prefix_list.append(temp)

print("mylsit: ", mylist)
print("prefix_list: ", prefix_list)

sum24 = prefix_list[4] - prefix_list[1]
print("sum24", sum24)