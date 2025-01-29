class RecentCounter:

    def __init__(self):
        self.request = []

    def ping(self, t: int) -> int:
        self.request.append(t)
        start = t - 3000
        end = t
        cnt = sum([1 for p in self.request if start < p < end])
        return cnt



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)