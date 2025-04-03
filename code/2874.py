class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pref_max = [nums[0]]
        suf_max = [nums[-1]]
        n = len(nums)
        for i in range(1, n):
            pref_max.append(max(nums[i], pref_max[i-1]))
            suf_max.append(max(nums[n-i-1], suf_max[i-1]))
        suf_max = suf_max[::-1]
        best = 0
        for j in range(1, n-1):
            best = max(best, (pref_max[j-1] - nums[j]) * suf_max[j+1])
        return best
