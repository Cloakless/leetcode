class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        if (sum(nums1) + nums1.count(0) > sum(nums2) and nums2[0] != 0) or (sum(nums2) + nums2.count(0)  > sum(nums1) and nums1[0] != 0):
            return -1
        s1, s2 = 0, 0
        for num in nums1:
            s1 += max(num, 1)
        for num in nums2:
            s2 += max(num, 1)
        return max(s1, s2)
        
