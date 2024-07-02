def solution(prices):
    length  = len(prices)
    answer = [i for i in range(length-1, -1, -1)]
    stack = [0]

    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    return answer