class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        a, b = int(num), int(num)

        for ns in num_str:
            if ns != "9":
                a = int(num_str.replace(ns, "9"))
                break
        
        for idx, ns in enumerate(num_str):
            if idx == 0 and ns != "1":
                b = int(num_str.replace(ns, "1"))
                break
            elif idx > 0 and ns != "0" and num_str[0] != ns:
                b = int(num_str.replace(ns, "0"))
                break

        return a - b