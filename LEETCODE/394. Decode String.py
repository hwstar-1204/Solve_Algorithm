class Solution:
    def decodeString(self, es: str) -> str:
        stack = []
        num = 0
        curr = ''

        for s in es:
            if s.isdigit():
                num = num * 10 + int(s)
            elif s == '[':
                stack.append((num, curr))
                num = 0
                curr = ''
            elif s == ']':
                repeat_cnt, last_string = stack.pop()
                curr = last_string + curr * repeat_cnt
            else:
                curr += s
        
        return curr