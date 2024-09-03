class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        sentences = [[] for _ in range(n)]
        words = set(wordDict)
        for i in reversed(range(n)):
            if s[i:] in words:
                sentences[i].append(s[i:])
            for j in range(1, n-i+1):
                if s[i:i+j] in words:
                    if i + j < n:
                        for sentence in sentences[i+j]:
                            sentences[i].append(s[i:i+j] + " " + sentence)
        return sentences[0]
