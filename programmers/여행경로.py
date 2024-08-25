from collections import defaultdict
def solution(tickets):
    answer = []
    place_dict = defaultdict(list)
    
    for ticket in tickets:
        s,e = ticket
        place_dict[s].append(e)            
    
    for i in place_dict.values():
        i.sort(reverse=True)
    
    stack = ['ICN']
    while stack:
        start = stack.pop()
        answer.append(start)
        
        goto_list = place_dict[start]
        stack += goto_list
        if place_dict[start]:
            place_dict[start].pop()
        
    return answer