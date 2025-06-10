class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd, min_even = 0, float("inf")

        for chr in set(s):
            n = s.count(chr)
            if n % 2 and n > max_odd:
                max_odd = n
            elif not n % 2 and n < min_even:
                min_even = n

        return max_odd - min_even
