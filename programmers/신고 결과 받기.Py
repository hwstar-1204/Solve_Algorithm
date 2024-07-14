"""  (1. 딕셔너리, 2. 2차원 배열)
딕셔너리 구조 "이름" : set()

신고한 사람 : 신고 당한 사람 리스트 
신고 당한 사람 : 신고한 사람 리스트 

"muzi frodo"
dict1[muzi].append(frodo)
dict2[frodo].append(muzi)

정지 id list = dict2에서 value의 길이가 k이상인 key 리스트

dict1에서 key에 해당하는 value리스트(신고당한 사람 리스트)에서 정지 id list에 있는 사람들 개수 구하기
dict1[id] = 찾은 정지 Id 개수 

for i, id in enumerate(id_list):
    id_list[i] = dict1[id]

"""
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    reporter_dict = defaultdict(set) 
    reported_dict = defaultdict(set) 
    
    for record in report:
        r, d = record.split()
        reporter_dict[r].add(d)
        reported_dict[d].add(r)

    print(reporter_dict)
        
    stop_list = []
    for id, ids in reported_dict.items():
        if len(ids) >= k:
            stop_list.append(id)
            
    for reporter_id, ids in reporter_dict.items():
        cnt = 0
        for reported_id in ids:
            if reported_id in stop_list:
                cnt += 1
        reporter_dict[reporter_id] = cnt
        
    for i, id in enumerate(id_list):
        id_list[i] = reporter_dict[id]

    print(reporter_dict)
               
    return id_list


def solution2(id_list, report, k):
    length = len(id_list)
    answer = [0] * length
    key_mapping = {id: i for i,id in enumerate(id_list)}
    report_arr = [[0] * length for _ in range(length)]
    
    for record in report:
        reporter, reported = map(lambda x: key_mapping[x], record.split())
        if not report_arr[reporter][reported]:
           report_arr[reporter][reported] = 1

    stop_list = []
    for i in range(length):
        cnt = 0
        for j in range(length):
            cnt += report_arr[j][i]
        if cnt >= k:
            stop_list.append(i)

    for i in range(length):
        for j in range(length):
            if report_arr[i][j] and j in stop_list:
                answer[i] += 1

    return answer
        
id_list = ["muzi", "frodo", "apeach", "neo"]	
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
k = 2

print(solution2(id_list, report, k))