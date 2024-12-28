class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = []
        i, tot = 0, 0
        n = len(nums)
        while i < k:
            tot += nums[i]
            i += 1
        sums.append(tot)
        while i < n:
            tot += nums[i]
            tot -= nums[i-k]
            sums.append(tot)
            i += 1

        best_left = 0
        left_idx = 0
        left_sum = []
        best_right = 0
        right_idx = 0
        right_sum = []
        for idx, window in enumerate(sums):
            if window > best_left:
                best_left = window
                left_idx = idx
            left_sum.append(left_idx)
        for idx in reversed(range(len(sums))):
            window = sums[idx]
            if window >= best_right:
                best_right = window
                right_idx = idx
            right_sum.append(right_idx)
        right_sum = right_sum[::-1]

        best = 0
        # Fix middle segment
        for j in range(k, n - 2*k+1):
            cand = sums[left_sum[j-k]] + sums[j] + sums[right_sum[j+k]]
            if cand > best:
                best_idx = [left_sum[j-k], j, right_sum[j+k]]
                best = cand
        return best_idx
