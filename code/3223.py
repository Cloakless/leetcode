class Solution:
    def minimumLength(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        ans = 0
        for c in counter:
            ans += min(2 - counter[c] % 2, counter[c])
        return ans
