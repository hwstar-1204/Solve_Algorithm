from itertools import permutations
N = input()
N_list = list(N)

candidates = sorted(list(permutations(N_list,len(N_list))))
for num in candidates:
    str_num = ''.join(num)
    if int(str_num) > int(N):
        print(int(str_num))
        break