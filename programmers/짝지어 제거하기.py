def solution(s):
    stack = []
    
    for i in s:
        if not i in stack or stack[-1] != i:
            stack.append(i)
            continue
        
        if stack[-1] == i:
            stack.pop()
                
    return 1 if not stack else 0