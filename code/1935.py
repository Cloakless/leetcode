class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        badders = set(brokenLetters)
        count = 0
        words = text.split()
        for word in words:
            bad = False
            for c in word:
                if c in badders:
                    bad = True
            if not bad:
                count += 1
        return count
