n = int(input())
n_list = [0]*12

#초기화
for i in range(1,4):
    n_list[i] = 2**(i-1)

for j in range(4,12):
    n_list[j] = n_list[j-3] + n_list[j-2] + n_list[j-1]

for _ in range(n):
    print( n_list[int(input())] )


# n_list[0] = 0
# n_list[1] = 1
# n_list[2] = 2
# n_list[3] = 4

# n_list[4] = 1+2+4=7
# n_list[5] = 2+4+7 = 13
# n_list[6] = 4+7+13 = 24
# n_list[7] = 7+13+24 = 44