from typing import List


class Solution:
    # 13ms
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candies[j] = max(candies[j], candies[j+1] + 1)

        return sum(candies)

    # 초기 - 19ms
    def candy(self, ratings: List[int]) -> int:
        nums = len(ratings)
        candies = [1 for _ in range(nums)]

        for i in range(nums - 1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1

        for j in range(nums-1, 0, -1):
            if ratings[j] < ratings[j-1]:
                candies[j-1] = candies[j] + 1
        
        for k in range(1, nums-1):
            if ratings[k-1] < ratings[k] and ratings[k] > ratings[k+1]:
                candies[k] = max(candies[k-1] + 1, candies[k+1] + 1)

        return sum(candies)