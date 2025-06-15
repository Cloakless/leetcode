class Solution:
    def maxDiff(self, num: int) -> int:
        def replace(x, a, b):
            x = str(x)
            ans = ''
            for c in x:
                if c == a:
                    ans += b
                else:
                    ans += c
            return int(ans)
        best, worst = 0, 10000000000
        ds = len(str(num))
        for i in range(10):
            for j in range(10):
                cand = replace(num, str(i), str(j))
                if cand != 0 and len(str(cand)) == ds:
                    best = max(best, cand)
                    worst = min(worst, cand)
        return best - worst
