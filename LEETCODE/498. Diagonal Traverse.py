from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(mat), len(mat[0])

        for cnt in range(n+m-1):
            tmp_list = []
            for i in range(cnt+1):
                if 0 <= i < n and 0 <= cnt-i < m:
                    tmp_list.append(mat[i][cnt-i])
            
            ans += tmp_list if cnt % 2 else tmp_list[::-1]

        return ans
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans, d = [], {}
        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m):
                total, num = i+j, mat[i][j]
                if total not in d:
                    d[total] = [num]
                else:
                    d[total].append(num)
        
        for key, diag_nums in d.items():
            print(diag_nums)
            ans += diag_nums if key % 2 else diag_nums[::-1]

        return ans



mat = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
res = s.findDiagonalOrder(mat)
print(res)
# Output: [1,2,4,7,5,3,6,8,9]
