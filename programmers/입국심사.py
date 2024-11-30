def solution(n, times):
    min_time = min(times)
    max_time = min_time * n
    
    while (min_time <= max_time):
        mid = (max_time + min_time) // 2
        capacity = sum([mid//t for t in times])
        
        if capacity < n:
            min_time = mid + 1
        else:
            max_time = mid - 1
            
    return min_time