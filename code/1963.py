class Solution:
    def minSwaps(self, s: str) -> int:
        tot = 0
        bs = list(s)
        worst = 0
        for i in range(len(bs)):
            if bs[i] == '[':
                tot += 1
            elif bs[i] == ']':
                tot -= 1
                if tot < 0:
                    worst = max(worst, -1*tot)
        return (worst+1)//2
