class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        n = len(nums)
        best = 1
        max_vals, min_vals = deque(), deque()
        while right < n:
            # Remove stuff which will never be worse than nums[right]
            while max_vals and max_vals[-1][1] < nums[right]:
                max_vals.pop()
            while min_vals and min_vals[-1][1] > nums[right]:
                min_vals.pop()
            max_vals.append((right, nums[right]))
            min_vals.append((right, nums[right]))
            # Make the widest array which ends in nums[right]
            while max_vals[0][1] - min_vals[0][1] > limit:
                left += 1
                if max_vals[0][0] < left:
                    max_vals.popleft()
                if min_vals[0][0] < left:
                    min_vals.popleft()
            best = max(best, right - left + 1)
            right += 1
        return best
