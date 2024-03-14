#잃어버린 괄호
"""
10 - 20 + 30 - 40
10 20+30 40
10 -  (20+30) - 40 
"""

sik = list(input().split('-'))
for i,s in enumerate(sik):
    if '+' in s:
        tmp = sum(list(map(int,s.split('+'))))
        sik[i] = tmp
    else:
        sik[i] = int(s)

answer = sik[0] - sum(sik[1:])
print(answer)