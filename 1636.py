class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = {}
        for item in nums:
            if item in freqs:
                freqs[item] += 1
            else:
                freqs[item] = 1
        nums.reverse()
        return sorted(nums, key=lambda x: freqs[x]-x/10000)
