from itertools import product

def solution(word):
    alpha = ["A","E","I","O","U"]
    result = []
    for i in range(1,6):
        # w = list(product(alpha, repeat=i))
        # words.extend(w)
        result += [''.join(item) for item in list(product(alpha, repeat=i))]

    result.sort()
    return result.index(word) + 1
