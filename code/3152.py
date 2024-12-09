class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        carry = nums[0]
        idxs = [0]
        c_index = 0
        for i in range(1, n):
            if (nums[i] % 2) == (nums[i-1] % 2):
                c_index = i
            idxs.append(c_index)
        ans = []
        for query in queries:
            if idxs[query[1]] == idxs[query[0]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
