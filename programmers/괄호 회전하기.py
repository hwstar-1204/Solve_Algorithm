"""
결과 = 0

각 괄호 dict 만들기 
배열 업데이트: s 문자열을 앞부분을 한칸씩 때서 뒤로 보냄
배열이 올바른 괄호인지 확인 
올바르면 결과+1

return 결과
"""

def valid_s(s):
    val_dict = { '[':']', '(':')', '{':'}' }
    stack = []
    
    for i in s:
        if i in val_dict.keys(): # 열린 괄호
            stack.append(i)
        else: # 닫힌 괄호
            if (not stack) or (val_dict[stack[-1]] != i):
                return False
            else:
                stack.pop()
    
    return True
                    

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        tmp_s = s[i:] + s[:i]
        print(tmp_s)

        if valid_s(tmp_s):
            answer += 1
            
    return answer
        

s = "}]()[{"

print(solution(s))