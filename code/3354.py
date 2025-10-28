class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        def is_valid(arr, pos, dire):
            arr = arr.copy()
            count = sum(arr)
            if count == 0:
                return True
            n = len(arr)
            if pos < 0 or pos >= n or arr[pos] != 0:
                return False
            while count > 0:
                if pos < 0 or pos > n-1:
                    return False
                if arr[pos] == 0:
                    pos += dire
                else:
                    arr[pos] -= 1
                    dire *= -1
                    pos += dire
                    count -= 1
            return True
        k = len(nums)
        for i in range(k):
            if nums[i] == 0:
                if is_valid(nums, i, 1):
                    ans += 1
                if  is_valid(nums, i, -1):
                    ans += 1
        return ans

        
