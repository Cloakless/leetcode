class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        best = max(counter.values())
        return max(counter.values())*sum([int(counter[x] == best) for x in counter])
