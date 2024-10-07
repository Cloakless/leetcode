class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        ans = 0
        if m % 2 != 0:
            for num in nums2:
                ans ^= num
        if n % 2 != 0:
            for num in nums1:
                ans ^= num
        return ans
