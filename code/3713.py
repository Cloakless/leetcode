class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        best = 0
        for i in range(n):
            count = defaultdict(int)
            for j in range(i,n):
                count[s[j]] += 1
                if len(set(count.values())) == 1:
                    best = max(best, j - i + 1)
        return best
