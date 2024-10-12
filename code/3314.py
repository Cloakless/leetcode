class Solution:
    @cache
def find_num(n):
    for i in range(n):
        if (i | (i+1)) == n:
            return i
        return -1
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(Solution.find_num(num))
        return ans
