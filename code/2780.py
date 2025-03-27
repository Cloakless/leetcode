class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s_nums = sorted(nums)
        elem = s_nums[n//2]
        elem_count = 0
        tot_count = nums.count(elem)
        idx = -1
        while idx < n - 1:
            idx += 1
            if nums[idx] == elem:
                elem_count += 1
            if elem_count > (idx + 1) // 2 and (tot_count - elem_count) > (n - idx - 1) // 2:
                return idx
        return -1
