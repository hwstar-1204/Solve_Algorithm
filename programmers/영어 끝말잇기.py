"""
answer = [0,0]
for i in range(1, len(words)-1):
    앞 뒤 단어 이어지는지 확인 
    현재 단어가 이미 나왔던거지 확인 -> set() 
    
    둘중 하나라도 안되면 아래 판단 후 answer 반환 및 종료  

        몇번째 사람인지 123 123
            i % n + 1

        몇번째 턴인지 111 222 333
             i // n + 1
             
return answer
"""
def solution(n, words):
    answer = [0,0]
    already_words = set()
    already_words.add(words[0])
    
    for i in range(1, len(words)):
        pre_alpa = words[i-1][-1]
        now_alpa = words[i][0]
        
        pre_length = len(already_words)
        already_words.add(words[i])
        now_length = len(already_words)

        if pre_alpa == now_alpa and pre_length != now_length:
            continue
        else:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
            
    return answer
