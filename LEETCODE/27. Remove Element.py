from typing import List


class Solution:
    # v1
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1

        if not nums: return 0
        
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return left
    
    # v2
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)