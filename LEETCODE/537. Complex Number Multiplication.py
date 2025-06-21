class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num):
            real, imag = num[:-1].split("+")
            return int(real), int(imag)
        
        a, b = parse(num1)
        c, d = parse(num2)
        real = a * c - b * d
        imag = a * d + b * c
        return f"{real}+{imag}i"