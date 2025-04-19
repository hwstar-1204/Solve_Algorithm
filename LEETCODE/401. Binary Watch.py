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

    def readBinaryWatch3(self, turnedOn: int) -> List[str]:
            result = []

            def backtrack(leds, index, turned_on):
                if turned_on == turnedOn:
                    hour = int("".join(map(str, leds[:4])), 2)
                    minute = int("".join(map(str, leds[4:])), 2)
                    if hour < 12 and minute < 60:
                        result.append(f"{hour}:{str(minute).zfill(2)}")
                    return

                for i in range(index, 10):
                    leds[i] = 1
                    backtrack(leds, i + 1, turned_on + 1)
                    leds[i] = 0

            backtrack([0] * 10, 0, 0)
            return result
