class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        counter = defaultdict(int)
        counter[nums[0]] += 1
        num_distinct = 1
        i, j, n = 0, 0, len(nums)
        best = 0
        tot = nums[0]
        while j < k - 1:
            j += 1
            counter[nums[j]] += 1
            tot += nums[j]
            if counter[nums[j]] == 1:
                num_distinct += 1
            if num_distinct == k:
                best = max(best, tot)
        while j < n - 1:
            j += 1
            tot += nums[j]
            if counter[nums[j]] == 0:
                num_distinct += 1
            counter[nums[j]] += 1
            tot -= nums[i]
            if counter[nums[i]] == 1:
                num_distinct -= 1
            counter[nums[i]] -= 1
            i += 1
            if num_distinct == k and tot > best:
                best = tot
        return best
