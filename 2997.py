class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        run = k
        for num in nums:
            run = run ^ num
        return bin(run).count('1')
