from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        for n in set(nums):
            if self.is_prime(nums.count(n)):
                return True
        return False

    def is_prime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True if num != 1 else False
