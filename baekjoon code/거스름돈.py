#거스름돈


#백트래킹1
change = int(input())
max_c = change // 5
cnt = 0
for i in range(0,max_c+1):
    if (c := change - 5*i) % 2 == 0:
        cnt = i + (c//2)

print(-1 if cnt == 0 else cnt)

#백트래킹2
change = int(input())
max_c = change // 5
cnt = float('inf')

for i in range(max_c,-1,-1):
    if (c := change - 5*i) % 2 == 0:
        # if cnt > i+(c//2):
        cnt = i+(c//2)
print(-1 if cnt == float('inf') else cnt)

#그리디
change = int(input())
cnt = 0

while change>0:
    if change % 5 == 0:
        cnt += change // 5
        break
    change -= 2
    cnt += 1

print( -1 if change < 0 else cnt)