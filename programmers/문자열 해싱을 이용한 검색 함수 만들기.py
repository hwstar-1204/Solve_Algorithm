"""
string_list = 문자열 리스트 
query_list = 쿼리 리스트 

각 쿼리 리스트에 있는 문자열이 string_list에 있는지 여부 확인
있으면 True, 없으면 False
"""

def polynominal_hash(str):
    p = 31
    m = 1000000007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value

def solution(string_list, query_list):
    hash_list = [polynominal_hash(str) for str in string_list]

    result = []
    for query in query_list:
        query_hash = polynominal_hash(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)
    
    return result


string_list = ["apple", "banana", "truck"]
query_list = ["apple","truck","answer"]

print(solution(string_list, query_list)) 

