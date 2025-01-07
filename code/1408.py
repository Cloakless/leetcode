class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for word in words:
            for word2 in words:
                if word != word2 and word in word2:
                    ans.add(word)
        return list(ans)
