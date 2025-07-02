def solution(stones, k):
    def can_cross(mid):
        skip = 0
        for s in stones:
            if s < mid:
                skip += 1
            else:
                skip = 0
            
            if skip >= k:
                return False
        return True
        
        
    ans = 1
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans
    