class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set()
        for num in nums:
            num_set.add(int(num, 2))

        cand = 0
        while cand in num_set:
            cand += 1
        base = bin(cand)[2:]
        while len(base) < n:
            base = '0' + base
        return base
