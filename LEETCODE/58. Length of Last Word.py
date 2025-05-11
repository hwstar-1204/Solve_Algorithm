class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        for i in range(len(words)-1, -1, -1):
            word = words[i]
            if  word == '':
                continue
            return len(word)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])
