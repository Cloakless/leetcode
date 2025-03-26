class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        counter = defaultdict(int)
        nums = []
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                counter[grid[a][b] % x] += 1
                nums.append(grid[a][b])
        if len(counter) > 1:
            return -1
        
        nums.sort()
        ans = 0
        median = nums[len(nums)//2]
        for num in nums:
            ans += abs(median - num)//x

        return ans
