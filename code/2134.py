class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        tot = sum(nums)
        nums = deque(nums)
        run, best = tot, tot
        for i in range(tot):
            run -= int(nums[i] == 1)
        for _ in range(len(nums)):
            binned = nums.popleft()
            run -= int(binned == 0)
            nums.append(binned)
            run += int(nums[tot-1] == 0)
            best = min(best, run)
        return best
