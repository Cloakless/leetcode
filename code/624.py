class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        highs = []
        lows = []
        for i in range(len(arrays)):
            highs.append((arrays[i][-1], i))
            lows.append((arrays[i][0], i))
        highs.sort()
        lows.sort()
        if lows[0][1] != highs[-1][1]:
            return highs[-1][0] - lows[0][0]
        else:
            return max(highs[-2][0] - lows[0][0], highs[-1][0] - lows[1][0])
