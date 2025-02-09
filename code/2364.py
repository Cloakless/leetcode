class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        counter = defaultdict(int)
        ans = 0
        counter[nums[0]] += 1
        for i in range(1,n):
            cand = nums[i] - i
            ans += i - counter[cand]
            counter[cand] += 1
        return ans
