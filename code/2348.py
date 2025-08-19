class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        streak = 0
        for elem in nums:
            if elem == 0:
                streak += 1
            else:
                ans += streak*(streak+1)//2
                streak = 0
        ans += streak*(streak+1)//2
        return ans
