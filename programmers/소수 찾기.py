from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    num_list = []
    
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            n = int(''.join(num))
            if is_prime(n):
                num_list.append(n)

    return len(set(num_list))
    