# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 2422
"""
1~n 종류의 아이스크림을 먹는데 함께 먹으면 맛이없는 조합을 피하면서 3가지 종류를 선택하는 방법 
입력
(1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)
n: 아이스크림 종류, m: 섞어먹으면 안되는 조합의 수 
출력
가능한 방법의 총 수 

idea
5c3 = 10
5-2 = 3 -> 123 124 125
5-2 = 3 -> 132 134 135
5-2 = 3 -> 341 342 345

1->2,3 123 124 125, 134 135 132/ 1234 1235 1245
2->1   213 214 215
3->1,4
4->3


1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5 t

2 3 4
2 3 5 t
2 4 5 t

3 4 5
전체 조합의 수(5c3) - 안되는 조합의 경우의 수(3+3+3) + 겹치는 수(2) = 3
sudo 

1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5

O(nlogn)
for i in range(1, n-1)
    for j in range(i+1, n)
        if (i,j) not in m_list:
        #     result += n-j

            for k in range(j+1, n+1)
                if [j,k] not in m_list:
                    cnt += 1
                
                
a = [ (i,j) (i,k) (j,k)]
        
nC3 - 안되는수
10 - 3-2-

"""
# ver 1
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# m_list = [list(map(int,input().split())) for _ in range(m)]
# cnt = 0

# for i in range(1, n-1):
#     for j in range(i+1, n):

#         if [i,j] not in m_list:
#             for k in range(j+1, n+1):
#                 if [j,k] not in m_list:
#                     cnt += 1
# print(cnt)



# ver 2 848ms
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# m_list = [[] for _ in range(n+1)]
# cnt = 0

# for _ in range(m):
#     no1, no2 = map(int,input().split())
#     m_list[no1].append(no2)
#     m_list[no2].append(no1)

# for i in range(1, n-1):
#     for j in range(i+1, n):

#         if j not in m_list[i]:
#             for k in range(j+1, n+1):
#                 if k not in m_list[j] and k not in m_list[i]:
#                     cnt += 1

# print(cnt)

# ver3 240ms
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
m_list = [[True]*(n+1) for _ in range(n+1)]
cnt = 0

for _ in range(m):
    no1, no2 = map(int,input().split())
    m_list[no1][no2] = False
    m_list[no2][no1] = False

for i in range(1, n-1):
    for j in range(i+1, n):

        if m_list[i][j]:
            for k in range(j+1, n+1):
                if m_list[i][k] and m_list[j][k]:
                    cnt += 1

print(cnt)