class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        tot = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                tot += 1
        return tot
