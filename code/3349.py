class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def is_increasing(arr):
            n = len(arr)
            for i in range(n-1):
                if arr[i+1] <= arr[i]:
                    return False
            return True

        for i in range(n):
            a = i
            b = i + k
            c = b + k
            if k == 1 and is_increasing(nums[a:b]):
                return True
            if c <= n and is_increasing(nums[a:b]) and is_increasing(nums[b:c]):
                return True 
        return False
