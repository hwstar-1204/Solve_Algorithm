#풍선 터트리기 
"""
1부터 N까지 풍선을 원형으로 존재 (n->1->2->... n)
각 풍선안에 -n <= 숫자 <= n 존재 (단 0은 없음)

제일 먼저 1번 풍선 터트리고 안에 있는 숫자 만큼 이동 하여 풍선 터트리기
단 터진 풍선으로 이동하는것은 이동횟수에 포함 X 

출력: 터진 풍선의 번호 차례대로
"""

n = int(input())
ballon = list(enumerate((map(int,input().split())), start = 1))
idx = 0

while ballon:
    now_idx, move = ballon.pop(idx)
    print(now_idx, end=' ')

    if move < 0 and ballon:
        idx = (idx + move) % len(ballon)
    elif move > 0 and ballon:
        idx = (idx + (move -1)) % len(ballon)
