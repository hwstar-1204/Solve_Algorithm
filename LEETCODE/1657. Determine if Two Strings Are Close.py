from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        same_len = len(word1) == len(word2)
        same_set = set(word1) == set(word2)
        if not same_len or not same_set:
            return False

        word1_dict = defaultdict(int)
        word2_dict = defaultdict(int)

        for w1 in word1:
            word1_dict[w1] += 1
        for w2 in word2:
            word2_dict[w2] += 1

        v1 = sorted([v for v in word1_dict.values()])
        v2 = sorted([v for v in word2_dict.values()])

        if not v1 == v2:
            return False
        
        return True