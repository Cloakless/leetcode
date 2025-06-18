class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            cand = [nums[i], nums[i+1], nums[i+2]]
            if cand[2] - cand[0] > k:
                return []
            ans.append(cand)
            i += 3
        return ans
