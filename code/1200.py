class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        min_dist = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            min_dist = min(min_dist, nums[i+1]-nums[i])
        ans = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == min_dist:
                ans.append([nums[i], nums[i+1]])
        return ans
