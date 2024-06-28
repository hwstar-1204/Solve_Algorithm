"""
4가지 명령어 U,D,R,L
(0,0) 에서 시작 (-5 <= x,y <= 5)

"""

def valid_load(x,y):
    return (0 <= x <= 10) and (0 <= y <= 10)
        
def move(x,y,m):
    if m == 'U':
        y += 1
    elif m == 'D':
        y -= 1
    elif m == 'R':
        x += 1
    else:
        x -= 1
        
    return x,y

def solution(dirs):
    foots = set()
    x,y = 5,5

    for m in dirs:
        mx, my = move(x,y,m)
        
        if not valid_load(mx,my):
            continue
            
        foots.add((x,y,mx,my))
        foots.add((mx,my,x,y))
        x,y = mx,my

    return len(foots) // 2