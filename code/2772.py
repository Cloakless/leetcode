class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        amount_subtracted = 0
        for i, elem in enumerate(nums):
            if amount_subtracted > elem:
                return False
            nums[i], amount_subtracted = elem - amount_subtracted, elem
            if i >= k - 1:
                amount_subtracted -= nums[i-k+1]
        return amount_subtracted == 0
