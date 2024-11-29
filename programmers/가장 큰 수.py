def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x*2)
        
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5, 9]	
result = solution(numbers)
print(result) # 9534330