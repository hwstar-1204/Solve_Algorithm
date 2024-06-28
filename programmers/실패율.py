"""
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수 
n : 스테이지 개수 (1 <= n <= 500)
stage : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열  (1 <= stage <= 200,000)

    n+1 = n번째 스테이지까지 클리어한 사용자 

출력 : 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 담긴 배열 
조건 : 실패율이 같은 스테이지는 작은 번호순 
      스테이지에 도달한 유저가 없는 경우 0으로 정의 

실패율 리스트 = [0] * N 
스테이지 정렬  1,2,2,2,3,3,4,6

""" 

def solution(N, stages):
    challengers = [0] * (N+2)  
    
    for i in stages:  # 각 스테이지에 도전한 사람 수 
        challengers[i] += 1
        
    # 각 스테이지에 실패한 사람 수 
    fails = {} # 실패 확률
    total = len(stages)  # 전체 도전자 수 
    
    for i in range(1, N+1):
        if challengers[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challengers[i] / total
            total = total - challengers[i]
            
    answer = sorted(fails, key=lambda x: fails[x], reverse=True)
    
    return answer
