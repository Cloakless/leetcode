class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        switches = 0
        curr = float('-inf')
        if len(nums) > 1 and nums[1] < nums[0]:
            return False
        for num in nums:
            if switches == 0:
                if num < curr:
                    switches += 1
                elif num == curr:
                    return False
                curr = num
            elif switches == 1:
                if num > curr:
                    switches += 1
                elif num == curr:
                    return False
                curr = num
            else:
                if num <= curr:
                    return False
                curr = num
        return switches == 2

            
