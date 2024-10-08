class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        if value == 1:
            return len(nums)
        lst = []
        added = set()
        for num in nums:
            cand = num % value
            while cand in added:
                cand += value
            lst.append(cand)
            added.add(cand)
        lst.sort()
        for i in range(len(lst)):
            if lst[i] != i:
                return i
        return len(lst)
