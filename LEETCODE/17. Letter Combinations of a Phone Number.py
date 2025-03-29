from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        en = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        maps = {str(i): en[i] for i in range(2, 10)}

        combinations = [""]
        for digit in digits:
            new_combinations = []
            for combination in combinations:
                for letter in maps[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations

        return combinations
