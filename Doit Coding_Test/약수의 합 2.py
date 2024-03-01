#약수의 합 2

# 1 2 5 10
"""
1 2 3 4 5 6 7 8 9 10 
1 
1 2
1 3
1 2 4
1 5
1 2 3 6
1 2 5 10


1부터 n+1까지 1로 저장해놓은 1차원 배열 

for n+1까지 반복하면서 
    소수이면 
        해당 배열+=자기자신 저장 
    아니면 
        짝수이면 
            배열[자기자신] += 배열[자기자신/2]
        홀수이면
            배열[자기자신] += 배열[자기자신/3]

출력: 해당 배열에 있는값을 모두 더한값 -1 (0번인덱스값 빼주기)

1 3 
1 5 
1 3 5 15 

"""
# import math
# n = int(input())
# fy = [i for i in range(n+1)]
# # fy[1] = 0

# for i in range(2,int(math.sqrt(n+1)+1)):
#     # if fy[i]%2 == 0: #소수이면 

#     #     continue
#     # else: #소수가 아니면
#     for j in range(i*i,n+2,i):
#         if fy[j]%2 == 0:       #짝수이면
#             fy[j] = fy[j/2] + j
#         elif fy[j]%2 == 1:                  #홀수이면
#             fy[j] = fy[j/3] + j

# answer = sum(fy) + ((n+1)//6)*2 #+1*(n+1)
# print(answer)

#다 더한값 + 1*(n+1) + ((n+1)//6)*2 


"""
2 2
3 3
4 2+4
5 5
6 3+6
7 7
8 2+4+8
9 3+9
10 5+10

12 3+6+12

24 3+6+12+24

1 2 3 4 6 12
"""


#소수이면 1로 아니면 자기자신으로 만들어야함


###

#n이하 자연수 중에서 i를 약수로 갖는 개수는 
"""
1 1
2 1 2
3 1 3
4 1 2 4
5 5 
6 1 2 3 6
"""
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i*(n//i)
# print(sum)

# print((lambda n: sum(i * (n // i) for i in range(1, n + 1))) (int(input())))

n = int(input())
print( sum(i*(n//i) for i in range(1,n+1)) )