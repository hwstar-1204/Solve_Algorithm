class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        upper = 0

        for i in range(max_len -1, -1, -1):
            total = int(a[i]) + int(b[i]) + upper
            result.append(str(total % 2))
            upper = total // 2

        if upper:
            result.append('1')

        return ''.join(reversed(result))

