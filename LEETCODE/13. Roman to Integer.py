class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ["I", "V", "X", "L", "C", "D", "M"]
        value = [1,5,10,50,100,500,1000]
        roman_dict = {s:v for s,v in zip(symbol, value)}

        ans = 0
        for i in range(len(s)-1,0,-1):
            if roman_dict[s[i]] > roman_dict[s[i-1]]:
                ans += roman_dict[s[i]] - 2*roman_dict[s[i-1]]
                continue
            ans += roman_dict[s[i]]

        return ans + roman_dict[s[0]]


    def romanToInt(self, s: str) -> int:
        symbol = ["I", "V", "X", "L", "C", "D", "M"]
        value = [1,5,10,50,100,500,1000]
        roman_dict = {s:v for s,v in zip(symbol, value)}

        sp_symbol = ["IV", "IX", "XL", "XC", "CD", "CM"]
        sp_symbol2 = ["IIII", "IIIIV", "XXXX", "XXXXL", "CCCC", "CCCCD"]
        change_symbol_dict = {s:v for s,v in zip(sp_symbol, sp_symbol2)}

        for ss in sp_symbol:
            s = s.replace(ss, change_symbol_dict[ss])

        return sum([roman_dict[chr] for chr in s])
