#일곱 난쟁이 
#for문을 이용하는 방법
# import sys
# input = sys.stdin.readline
# s = [int(input()) for _ in range(9)]
# s.sort()
# s_sum = sum(s)

# for i in range(8):
#     for j in range(i+1,9):
#         if s_sum-(s[i]+s[j]) == 100:
#             s[j] = 0
#             s[i] = 0
#             for k in s:
#                 if k != 0:
#                     print(k)
#             exit()




#조합 라이브러리를 이용하는 방법
import itertools
s = [int(input()) for _ in range(9)]

for i in itertools.combinations(s,7):
    if sum(i) == 100:
        for e in sorted(i):
            print(e)
        break