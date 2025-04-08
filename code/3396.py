class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        elems = set()
        bad = None
        for i in range(n):
            if nums[n-i-1] in elems:
                bad = n-i-1
                break
            else:
                elems.add(nums[n-i-1])
        if bad is None:
            return 0
        return (bad) // 3 + 1
