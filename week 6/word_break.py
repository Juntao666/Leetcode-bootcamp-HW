class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_set = set()
        for word in wordDict:
            len_set.add(len(word))
        word_set = set(wordDict)
        n = len(s)
        dp = [0] * n
        for i in range(n):
            for length in len_set:
                if i + 1 == length and s[:i + 1] in word_set:
                    dp[i] = 1
                    break
                if i >= length:
                    if s[i - length + 1 : i + 1] in word_set and dp[i - length] == 1:
                        dp[i] = 1
                        break
        return dp[n - 1] == 1