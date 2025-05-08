from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_dict and idx != num_dict[diff]:
                return [idx, num_dict[diff]]
