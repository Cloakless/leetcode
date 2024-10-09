class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        opt1 = True
        opt2 = True
        X = nums1[n-1]
        Y = nums2[n-1]
        tot1 = 0
        tot2 = 1
        for i in range(n-1):
            if nums1[i] <= X and nums2[i] <= Y:
                # No swaps needed
                pass
            elif nums1[i] <= Y and nums2[i] <= X:
                tot1 += 1
            else:
                opt1 = False
            if nums1[i] <= Y and nums2[i] <= X:
                # No swaps needed to be other way round
                pass
            elif nums1[i] <= X and nums2[i] <= Y:
                tot2 += 1
            else:
                opt2 = False
        if opt1 is False and opt2 is False:
            return -1
        if opt1 is True and opt2 is True:
            return min(tot1, tot2)
        if opt1 is True:
            return tot1
        else:
            return tot2
