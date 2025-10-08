class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        import bisect
        ans = []
        potions.sort()
        n = len(potions)
        for spell in spells:
            target = success / spell
            idx = bisect.bisect_left(potions, target)
            ans.append(n-idx)
        return ans
