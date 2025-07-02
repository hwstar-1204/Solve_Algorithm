from collections import Counter


def solution(want, number, discount):
    ans = 0
    cart = dict(zip(want, number))    

    for i in range(len(discount) - 9):
        if check_same(cart, Counter(discount[i:i+10])):
            ans += 1
    return ans

def check_same(cart, curr_sales):
    if cart.keys() != curr_sales.keys():
        return False

    for item, cnt in cart.items():
        if cnt > curr_sales[item]:
            return False
    
    return True