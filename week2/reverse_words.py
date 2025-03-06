class Solution:
    def reverseWords(self, s: str) -> str:
        splited_ls = s.split()
        splited_ls.reverse()
        return " ".join(splited_ls)