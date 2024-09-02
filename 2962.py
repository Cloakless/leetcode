class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxN = max(nums)
        if nums.count(maxN) < k:
            return 0
        ans = 0
        count = 0
        n = len(nums)

        l = 0
        r = 0
        # get initial window
        while count < k:
            if nums[r] == maxN:
                count += 1
            r += 1
        r -= 1

        while True:
            ans += (n - r)

            if nums[l] == maxN:
                count -= 1
            l += 1

            while count < k:
                # check next element
                r += 1
                if r >= n:
                    return ans
                # Find next maxN to the right
                if nums[r] == maxN:
                    count += 1
