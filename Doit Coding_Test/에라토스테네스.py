import math

# n = 2
# num_list = [i for i in range(2, pow(10, n) + 1)]  # 숫자 리스트 초기화

n = 2
num_list = [0]*(pow(10,n)+1)
num_list[0] = 0
num_list[1] = 1

for i in range(2,pow(10,n)+1):
    num_list[i] = i

def isPrimeES(num_list):
    for i in range(2, pow(10,n) + 1):
        if num_list[i] == 0:
            continue
        for j in range(2 * i, pow(10,n)+1, i):
            num_list[j] = 0

# 함수 호출
isPrimeES(num_list)

# 소수만 남기고 출력 또는 리스트로 추출
prime_numbers = [num for num in num_list if num != 0]

print("소수 리스트:", prime_numbers)
print(len(prime_numbers))

# def sieve_of_eratosthenes(limit):
#     primes = []
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, int(limit**0.5) + 1):
#         if is_prime[i]:
#             primes.append(i)
#             for j in range(i*i, limit + 1, i):
#                 is_prime[j] = False

#     for i in range(int(limit**0.5) + 1, limit + 1):
#         if is_prime[i]:
#             primes.append(i)

#     return primes

# n = 2
# limit = pow(10, n)
# prime_numbers = sieve_of_eratosthenes(limit)

# print("소수 리스트:", prime_numbers)

# print(len(prime_numbers))