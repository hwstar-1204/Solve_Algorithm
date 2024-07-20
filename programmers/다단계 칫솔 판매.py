# 다단계 칫솔 판매 

def solution(enroll, referral, seller, amount):
    answer = {name: 0 for name in enroll}
    parent = dict(zip(enroll, referral))
    
    for i in range(len(seller)):
        money = amount[i] * 100
        name = seller[i]
        
        while money and name != '-':
            tmp = money // 10
            answer[name] += money - tmp
            money = tmp
            name = parent[name]
    
    return [ answer[name] for name in enroll]