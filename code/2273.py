class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        n = len(words)
        for i in range(1, n):
            a, b = sorted(list(words[i])), sorted(list(words[i-1]))
            if a != b:
                ans.append(words[i])
        return ans
