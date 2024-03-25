#회의실 배정
"""
회의실 1개에서 n개의 회의를 최대한 많이 하도록 
정렬기준 
1. 끝나는시간 기준
2. 시작시간 기준

testcase
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

7
2 3
3 3
1 3
1 4
4 6
3 8
9 11


"""
import sys
input = sys.stdin.readline
n = int(input())
rooms = [0 for _ in range(n)]
answer = 1
for i in range(n):
    a,b = map(int,input().split())
    rooms[i] = (a,b)

rooms.sort(key=lambda x: (x[1],x[0])) # 끝나는 시간으로 오름차순 정렬 

# print(rooms)

end = rooms[0][1] #첫번째 회의 끝나는 시간
for i in range(1,n):
    start = rooms[i][0]
    if end <= start:
        end = rooms[i][1]
        answer += 1
    else:
        continue
print(answer)