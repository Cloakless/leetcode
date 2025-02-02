class Solution:
    def check(self, nums: List[int]) -> bool:
        rot = False
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                if not rot:
                    rot = True
                else:
                    return False
        return True
