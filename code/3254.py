class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def power(i,j):
            n = j - i + 1
            if nums[j] - nums[i] != n - 1:
                return -1
            if len(set(nums[i:j+1])) != n:
                return -1
            if sorted(nums[i:j+1]) != nums[i:j+1]:
                return -1
            return nums[j]

        ans = []
        for i in range(len(nums) - k + 1):
            ans.append(power(i, i + k - 1))
        return ans
