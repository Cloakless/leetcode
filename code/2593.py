class Solution:
    def findScore(self, nums: List[int]) -> int:
        elems = []
        for idx, num in enumerate(nums):
            heappush(elems, (num, idx))
        marked = set()
        score = 0
        while elems:
            num, idx = heappop(elems)
            if idx not in marked:
                score += num
                marked.add(idx)
                marked.add(idx+1)
                marked.add(idx-1)
        return score
