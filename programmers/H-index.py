# ver 1 
def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i + 1 > c:
            return i
    return len(citations)

# ver 2
from collections import defaultdict
def solution(citations):
    cnt_dict = defaultdict(int)
    for i in citations:
        cnt_dict[i] += 1

    citations = sorted(list(set(citations)), reverse=True)

    cumulation = 0
    for h in range(citations[0], -1, -1):
        if h in cnt_dict:
            cumulation += cnt_dict[h]
        
        if cumulation >= h:
            return h

    return 0