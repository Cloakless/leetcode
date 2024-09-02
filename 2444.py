class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK not in nums or maxK not in nums:
            return 0
        def splitList(nums, minK, maxK):
            split = []
            temp = []
            for i in range(len(nums)):
                val = nums[i]
                if val >= minK and val <= maxK:
                    temp.append(val)
                else:
                    if temp != []:
                        split.append(temp)
                        temp = []
            if temp != []:
                split.append(temp)
            return split

        def countSubs(nums, minK, maxK):
            count = 0
            n = len(nums)
            for i in range(n):
                seen_min = False
                seen_max = False
                j = i
                while (not (seen_min and seen_max)):
                    if j >= n:
                        break
                    if nums[j] == minK:
                        seen_min = True
                    if nums[j] == maxK:
                        seen_max = True
                    j += 1
                if seen_min and seen_max:
                    count += n - j + 1
            return count

        arrs = splitList(nums, minK, maxK)
        tot = 0
        for arr in arrs:
            tot += countSubs(arr, minK, maxK)
        return tot
        
