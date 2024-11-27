def solution(brown, yellow):
    """
    최소 3*3
    가로 >= 세로 

    brown + yellow = 가로*세로
    return [가로, 세로]

    48 = (3, 16) (4, 12) (6, 8)
    """
    
    w, h = 3, 3
    total = brown+yellow    

    for i in range(3, total):
        if total % i:
            continue
        h = i
        w = total // i
        
        # if (w+h) * 2 - 4 == brown and w*h - brown == yellow:
        if (w-2) * (h-2) == yellow:
            return [w,h]
        
data = [24, 24]
print(solution(*data))
