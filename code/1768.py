class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        m, n = len(word1), len(word2)
        for i in range(max(m, n)):
            if i < m:
                ans.append(word1[i])
            if i < n:
                ans.append(word2[i])
        return "".join(ans)
