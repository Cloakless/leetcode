class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xsum(arr):
            counter = defaultdict(int)
            for num in arr:
                counter[num] += 1
            freqs = []
            for num in counter:
                freqs.append((counter[num], num))
            freqs.sort(reverse=True)
            ans = 0
            for i in range(min(len(freqs), x)):
                ans += freqs[i][0] * freqs[i][1]
            return ans

        ans = []
        for i in range(len(nums)-k+1):
            ans.append(xsum(nums[i:i+k]))
        return ans
