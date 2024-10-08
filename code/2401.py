class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        best = 1
        i, j = 0, 0
        tracker = nums[0]
        while j < len(nums) - 1:
            j += 1
            if nums[j] & tracker == 0:
                best = max(best, j - i + 1)
                tracker ^= nums[j]
            else:
                broken = True
                while broken:
                    tracker ^= nums[i]
                    i += 1
                    if tracker & nums[j] == 0:
                        tracker ^= nums[j]
                        broken = False
        return best
