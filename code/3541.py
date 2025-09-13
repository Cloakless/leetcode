class Solution:
    def maxFreqSum(self, s: str) -> int:
        counterv = defaultdict(int)
        counterc = defaultdict(int)
        counterv['a'] = 0
        counterc['b'] = 0
        for c in s:
            if c in {'a', 'e', 'i', 'o', 'u'}:
                counterv[c] += 1
            else:
                counterc[c] += 1
        return max(counterc.values()) + max(counterv.values())
