class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [50] * n # Max inefficiency
        for i in range(n):
            if i > 0:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
            for word in dictionary:
                m = len(word)
                if i - m == -1 and s[:i+1] == word:
                    dp[i] = 0
                elif i - m + 1 >= 0:
                    if s[i+1-m:i+1] == word:
                        dp[i] = min(dp[i], dp[i-m])
        return dp[n-1]
