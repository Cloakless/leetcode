class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot = 0
        left = 0
        mid = 0
        while nums[mid] % 2 == 0:
            mid += 1
            if mid == n:
                return 0
        num_odd = 1
        right = mid
        while num_odd < k:
            right += 1
            if right == n:
                return 0
            if nums[right] % 2 == 1:
                num_odd += 1
        while right < n:
            tot += mid - left + 1
            right += 1
            if right == n:
                break
            if nums[right] % 2 == 1:
                left = mid + 1
                mid += 1
                while nums[mid] % 2 == 0:
                    mid += 1
        return tot
