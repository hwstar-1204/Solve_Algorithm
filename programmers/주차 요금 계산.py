"""
{key: 차량 번호  value: 입차 시간}
요금 계산 
if 입차 - 출차 <= 기본시간:
    기본 요금
else:
    기본요금 + ((출차 - 입차) / 단위시간) * 단위 요금  (반올림적용)
    
return 주차요금 배열 (정렬: 차량번호가 작은 순서) 

[(차량번호, 주차요금), ... ]
"""

        

from math import ceil

def calc_fee(total_time, fees):
    d_time, d_fee, u_time, u_fee = fees  # default, unit
    total_fee = d_fee
    
    if total_time <= d_time:
        return total_fee
    
    total_fee += ceil((total_time - d_time) / u_time) * u_fee
    return total_fee


def solution(fees, records):
    record_dict = {}  # {"차량번호" : [(시간), (시간), ...]}
    result = []
       
    for r in records:
        time, car_num, IO_type = r.split()
        h, m = time.split(":")
        time = int(h) * 60 + int(m)
        
        if not car_num in record_dict.keys():
            record_dict[car_num] = [time]
        else:
            record_dict[car_num].append(time)

    for car_num in record_dict:
        times = record_dict[car_num]

        if len(times) % 2:  # 입출이 홀수인경우
            times.append(23 * 60 + 59)  # 출차 시간을 23:59로 설정
            
        total_time = sum([(times[i+1] - times[i]) for i in range(0, len(times), 2)])
        fee = calc_fee(total_time, fees)
        result.append((car_num,fee))
        
    return [r[1] for r in result.sort()]
