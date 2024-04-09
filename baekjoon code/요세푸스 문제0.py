# 요세푸스 문제0
"""
1~n 명의 사람 원으로 앉음 
n명의 사람이 모두 제거될때 까지 양수 k 번째 사람 제거 

입력: n,k

1 2 4 5 7
if len < idx
    idx = idx-len+1
if n_list[idx]
    while n_list[idx] == 0
        idx += 1
n_list[idx] = 0
len보다 커지면 idx = idx-len-1
"""
n,k = map(int,input().split())
n_list = [i for i in range(1,n+1)]
idx = 0
answer = []

while n_list:
    idx += k - 1 
    if len(n_list) <= idx:
        idx = idx % len(n_list)
    answer.append(str(n_list.pop(idx)))
print('<' + ', '.join(answer) + '>')
