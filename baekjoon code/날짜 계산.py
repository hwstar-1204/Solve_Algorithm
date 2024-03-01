#날짜 계산 
"""
(1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
"""
year = list(map(int,input().split()))
init_year = [0,0,0]
ans = 0
while True:
    for i in range(3):
        init_year[i] += 1
        if init_year[i] > 15 and i == 0:
            init_year[i] = 1
        elif init_year[i] > 28 and i == 1:
            init_year[i] = 1
        elif init_year[i] > 19 and i == 2:
            init_year[i] = 1
    ans += 1
    if init_year == year:
        print(ans)
        break