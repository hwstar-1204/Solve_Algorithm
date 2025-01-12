from collections import defaultdict
from typing import List 

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        int_dict = defaultdict(int)
        for n in arr:
            int_dict[n] += 1

        set_values = [value for value in int_dict.values()]
        if len(set_values) == len(set(set_values)):
            return True
        return False