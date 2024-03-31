class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        arrs = 0
        curr_diff = 1
        tots = {num: 0 for num in nums}
        tots[nums[0]] = 1
        n = len(nums)
        # Make initial window
        while curr_diff < k:
            r += 1
            if r >= n:
                return arrs
            if tots[nums[r]] == 0:
                tots[nums[r]] = 1
                curr_diff += 1
            else:
                tots[nums[r]] += 1

        arrs += 1
        while True:
            # shift window right, check if still k distinct
            while True:
                r += 1
                if r >= n:
                    r -= 1
                    break
                if tots[nums[r]] == 0:
                    tots[nums[r]] += 1
                    curr_diff += 1
                    break
                else:
                    tots[nums[r]] += 1
                    arrs += 1
            
            # counter is k + 1, shift l up one
            tots[nums[l]] -= 1
            if tots[nums[l]] == 0:
                curr_diff -= 1
            l += 1
            while curr_diff >= k:
                tots[nums[r]] -= 1
                if tots[nums[r]] == 0:
                    curr_diff -= 1
                r -= 1
            r += 1
            if r >= n:
                return arrs
            tots[nums[r]] += 1
            curr_diff += 1
            arrs += 1
 
        return arrs


        
