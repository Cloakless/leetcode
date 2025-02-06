class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                counter[nums[i]*nums[j]] += 1
        ans = 0
        for prod in counter:
            ans += 8*(counter[prod]*(counter[prod]-1)//2)
        return ans
