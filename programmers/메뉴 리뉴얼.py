"""
이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
1. 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴
2. 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하
"""

# 코스에 속할 메뉴 개수 경우의 수 만큼 반복

    # order_dict = c가지 단품메뉴 골랐을 경우 : 빈도 수 로하는 딕셔너리 
    # orders 각각의 주문들에 대해 
        # 만약 c가 한사람이 주문한 단품 메뉴보다 크기가 크면 X
        
        # c(코스메뉴 개수)개 단품 메뉴를 고를 수 있는 경우의 수 반복
            # order_dict에서 각 경우의 수를 Key로 하여 개수(value)를 업데이트 

    # order_list = order_dict를 value 기준 내림차순

    # order_list에서 value가 1이면 안됨 무조건 2이상 (주문한 손님수 > 1)
    # order_list에서 가장 큰 값을 가진 값과 같은 값까지만 

    # answer에 추가


# answer 알파벳 오름차순 정렬


from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    for c in course:
        order_dict = defaultdict(int)

        for order in orders:
            menues = sorted(order)

            if c > len(menues):
                    continue

            for comb in combinations(menues, c):
                comb_key = ''.join(comb)
                order_dict[comb_key] += 1

        comb_list = sorted(list(order_dict.items()), key=lambda x: x[1], reverse=True)
        if not comb_list or comb_list[0][1] < 2:
            continue

        top_comb_list = []
        for comb,cnt in comb_list:
            if comb_list[0][1] == cnt:
                top_comb_list.append(comb)
            else:
                break

        answer += top_comb_list

    answer.sort()
    return answer

order = ["XYZ", "XWY", "WXA"]	
course = [2,3,4]	

print(solution(order,course))
