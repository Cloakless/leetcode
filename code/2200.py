class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                for j in range(max(0, i - k), min(i+k+1, n)):
                    ans.add(j)
        return sorted(list(ans))
