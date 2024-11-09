class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        best_k = 2**maximumBit - 1
        acc = 0
        ans = []
        for num in nums:
            acc ^= num
            ans.append(best_k^acc)
        return ans[::-1]
