class Solution:
    def trap(self, height: List[int]) -> int:
        best_left = []
        best_right = []
        bl = 0
        br = 0
        n = len(height)
        for i in range(n):
            bl = max(bl, height[i])
            br = max(br, height[n-i-1])
            best_left.append(bl)
            best_right.append(br)
        best_right = best_right[::-1]
        rain = 0
        for i in range(n):
            rain += min(best_left[i], best_right[i]) - height[i]
        return rain
