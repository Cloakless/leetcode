class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        ans = 0
        for num in counter:
            if (num + 1) in counter:
                ans = max(ans, counter[num] + counter[num+1])
        return ans
