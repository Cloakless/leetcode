class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        best = 10**6
        counts = [0] * 31

        def counts_val():
            ans = 0
            bit = 1
            for count in counts:
                ans += bit * int(count > 0)
                bit *= 2
            return ans
        
        def add_to_counts(val):
            bit_pos = 0
            while val > 0:
                counts[bit_pos] += val % 2
                bit_pos += 1
                val //= 2

        def remove_from_counts(val):
            bit_pos = 0
            while val > 0:
                counts[bit_pos] -= val % 2
                bit_pos += 1
                val //= 2
         
            
        add_to_counts(nums[0])
        if counts_val() >= k:
            return 1
        while counts_val() < k:
            right += 1
            if right >= len(nums):
                return -1
            add_to_counts(nums[right])

        best = right - left + 1
        while right < len(nums):
            while counts_val() >= k:
                best = min(best, right - left + 1)
                remove_from_counts(nums[left])
                left += 1
            while counts_val() < k:
                right += 1
                if right >= len(nums):
                    return best
                add_to_counts(nums[right])
