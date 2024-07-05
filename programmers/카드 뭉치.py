def solution(cards1, cards2, goal):
    for char in goal:
        if cards1 and cards1[0] == char:
            cards1.pop(0)
        elif cards2 and cards2[0] == char :
            cards2.pop(0)
        else:
            return "No"
    
    return "Yes"

from collections import deque

def solution2(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for char in goal:
        if cards1 and cards1[0] == char:
            cards1.popleft()
        elif cards2 and cards2[0] == char :
            cards2.popleft()
        else:
            return "No"
    
    return "Yes"

