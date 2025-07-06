def solution(s):
    
    def is_valid(s):
        stack = []
        OC_dict = {"(": ")", "{": "}", "[": "]"}
        
        for chr in s: 
            stack.append(chr)
            
            if len(stack) >= 2:
                if stack[-2] in OC_dict.keys() and OC_dict[stack[-2]] == chr:
                    stack = stack[:-2]
                
        return 1 if len(stack) == 0 else 0
                
                
    return sum([is_valid(s[i:] + s[:i]) for i in range(len(s))])