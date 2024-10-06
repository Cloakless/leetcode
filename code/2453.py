class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        rems = defaultdict(int)
        max_val = 0
        for num in nums:
            rems[num % space] += 1
            max_val = max(max_val, rems[num % space])
        best = 1000000000
        for num in nums:
            if rems[num%space] == max_val:
                best = min(best, num)
        return best
        
