import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1000 + 1)]
        heapq.heapify(self.nums)

    def popSmallest(self) -> int:
        return heapq.heappop(self.nums)

    def addBack(self, num: int) -> None:
        if num in self.nums:
            return None

        heapq.heappush(self.nums, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)