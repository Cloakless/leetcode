class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        opts = {0}
        for num in nums:
            news = []
            for thing in opts:
                news.append(thing + num)
            for new in news:
                opts.add(new)
        return target in opts

