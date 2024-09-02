class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def valid(arr, val):
            for num in arr:
                if abs(num - val) == k:
                    return False
            return True

        def tot_beautiful(i, arr):
            if i == n:
                return 1
            tot = 0
            cand = nums[i]
            if not valid(arr, cand):
                tot += tot_beautiful(i+1, arr)
            else:
                tot += tot_beautiful(i+1, arr+[cand]) + tot_beautiful(i+1, arr)
            return tot
        return tot_beautiful(0, []) - 1
