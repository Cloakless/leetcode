class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = [0 for _ in range(26)]
        for s in word:
            freqs[ord(s) - 97] += 1
        freqs.sort()
        freqs.reverse()
        print(freqs)
        return sum(freqs[:8]) + sum(freqs[8:16]) * 2 + sum(freqs[16:24]) * 3 + sum(freqs[24:]) * 4 
