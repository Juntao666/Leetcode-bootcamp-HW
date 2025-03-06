class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n_p = len(p)
        n_s = len(s)
        s_ls = list(s)
        p_ls = list(p)
        if n_s < n_p:
            return res
        dict_p = {}
        dict_s = {}
        i = 0
        while i < n_p:
            char_p = p_ls[i]
            char_s = s_ls[i]
            if dict_p.get(char_p, 0) == 0:
                dict_p[char_p] = 0
            dict_p[char_p] += 1
            if dict_s.get(char_s, 0) == 0:
                dict_s[char_s] = 0
            dict_s[char_s] += 1
            i += 1
        
        l = 0
        r = i
        while True:
            if dict_p == dict_s:
                res.append(l)
            if r == n_s:
                break
            char_to_pop = s_ls[l]
            char_to_add = s_ls[r]
            dict_s[char_to_pop] -= 1
            if dict_s[char_to_pop] == 0:
                del dict_s[char_to_pop]
            if dict_s.get(char_to_add, 0) == 0:
                dict_s[char_to_add] = 0
            dict_s[char_to_add] += 1
            l += 1
            r += 1
        
        return res