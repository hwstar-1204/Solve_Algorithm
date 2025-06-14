class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        max_num, min_num = int(num_str), int(num_str)
        for n in num_str:
            if n != '9':
                max_num = int(num_str.replace(n, '9'))
                break
        for n in num_str:
            if int(n) <= 9:
                min_num = int(num_str.replace(n, '0'))
                break 
        return max_num - min_num
