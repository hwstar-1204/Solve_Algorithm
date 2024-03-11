#블로그2
"""
연속된 임의의 문제를 선택
선택된 문제를 전부 같은 색으로 칠함 

푼문제 > 못푼문제 : 전체파랑 + 못푼문제 개수만큼 빨강 칠함 
푼문제 < 못푼문제 : 전체빨강 + 푼문제 개수만큼 파랑 칠함 

testcase
푼문제,못푼문제 개수 같을떄
bbrrbbrr : 4>3 한번에
brbbrrbr : 6>4 한번에
bbbrrbrr : 4>3 한번에

한쪽이 더 개수가 많을때 
brbrbrbrr : 8>5 한번에 
brbrbrrrb : 7>5 한번에
bbrbbrrrr : 4>3 한번에 
brbrrrrbb : 5>3 한번에

bbrbrbbr : 붙어있는거는 하나로 취급
brbrbr
현재와 다음꺼가 같으면:
    continue
현재와 다음꺼가 다르면:
    현재색 개수 + 1
"""
import sys
input = sys.stdin.readline
n = int(input())
problems = list(input().rstrip())
problems.append('dummy') 

color_dict = {'B':0, 'R':0}
for i in range(n):
    if problems[i] == problems[i+1]:
        continue
    else:
        color_dict[problems[i]] += 1

if color_dict['B'] > color_dict['R']:
    result = color_dict['R'] 
else:
    result = color_dict['B']

print(result + 1)


# print(input().rstrip().split('B'))