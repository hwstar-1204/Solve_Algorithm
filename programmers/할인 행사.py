def solution(want, number, discount):
    result = 0

    for i in range(len(discount) - 9):
        dict_n = {key: value for key, value in zip(want, number)}

        for j in range(i, i + 10):
            k = discount[j]
            if k in want and dict_n[k]:
                dict_n[k] -= 1
            else:
                break

        if not sum(dict_n.values()):
            result += 1
            
    return result

want = ["banana", "apple", "rice", "pork", "pot"]	
number = [3,2,2,2,1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	

print(solution(want,number,discount))
