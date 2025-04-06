class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        parents = defaultdict(set)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] % nums[j] == 0:
                    parents[nums[j]].add(nums[i])
                elif nums[j] % nums[i] == 0:
                    parents[nums[i]].add(nums[j])
        
        @cache
        def depth(k):
            if not parents[k]:
                return [k]
            else:
                best = []
                for x in parents[k]:
                    lst = depth(x)
                    if len(lst) > len(best):
                        best = lst
                return [k] + best

        ans = []
        for n in nums:
            a = depth(n)
            if len(a) > len(ans):
                ans = a
        return ans
        
