from typing import List
from itertools import product

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_one(n: int) -> int:
            return bin(n).count("1")
        
        ans = []
        for hour in range(12):
            for minute in range(60):
                if count_one(hour) + count_one(minute) == turnedOn:
                    time = f"{hour}:{str(minute).zfill(2)}"
                    ans.append(time)
        return ans

    def readBinaryWatch2(self, turnedOn: int) -> List[str]:
        def count_one(n: int) -> int:
            return bin(n).count("1")
        
        ans = []
        for hour, minute in product(range(12), range(60)):
            if count_one(hour) + count_one(minute) == turnedOn:
                time = f"{hour}:{str(minute).zfill(2)}"
                ans.append(time)
        return ans

