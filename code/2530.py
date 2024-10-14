class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -1*x, nums))
        heapq.heapify(nums)
        score = 0
        while k > 0:
            cand = -1*heapq.heappop(nums)
            score += cand
            heapq.heappush(nums, -1*math.ceil(cand/3))
            k -= 1
        return score
