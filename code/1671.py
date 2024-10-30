class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        increasings = [0] * n
        decreasings = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    increasings[i] = max(increasings[i], increasings[j] + 1)
        for x in reversed(range(n)):
            for y in range(x+1, n):
                if nums[y] < nums[x]:
                    decreasings[x] = max(decreasings[x], decreasings[y] + 1)
        best = 1
        for a in range(n):
            if increasings[a] > 0 and decreasings[a] > 0:
                best = max(best, increasings[a] + decreasings[a])
        return n - best - 1
