class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = 0
        store = defaultdict(list)
        for i in range(m):
            n = max(n, len(nums[i]))
            for j in range(len(nums[i])):
                cand = nums[i][j]
                store[i+j].append(cand)
        ans = []
        for k in range(m+n-1):
            for cand in store[k][::-1]:
                ans.append(cand)
        return ans
