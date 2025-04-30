class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([bool(len(str(num)) % 2 == 0) for num in nums])
