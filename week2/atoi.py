class Solution:
    def myAtoi(self, s: str) -> int:
        s_ls = list(s)
        n = len(s_ls)
        i = 0
        while i < n and s_ls[i] == " ":
            i += 1
        
        res = 0
        positive = True
        if i < n: 
            if s_ls[i] == "+" or s_ls[i] == "-":
                if s_ls[i] == "-":
                    positive = False
                i += 1
        
        while i < n:
            char = s_ls[i]
            if not char.isdigit():
                break
            else:
                if positive:
                    res = res * 10 + int(char)
                else:
                    res = res * 10 - int(char)
                if res >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                if res < -(2 ** 31):
                    return -(2 ** 31)
                i += 1
        
        return res