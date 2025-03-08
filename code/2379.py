class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        num_black = []
        tot = 0
        for block in blocks:
            if block == 'B':
                tot += 1
            num_black.append(tot)
        best = k - num_black[k-1]
        for i in range(len(blocks)-k):
            best = min(best, k - (num_black[i+k] - num_black[i]))
        return best
