class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        @cache
        def calc(n):
            if n == 2:
                return -1
            rep = list(bin(n)[2:])
            m = len(rep)-1
            while m > 0 and rep[m-1] == '1':
                m -= 1
            rep[m] = '0'
            return int(''.join(rep), 2)
        ans = []
        for num in nums:
            ans.append(calc(num))
        return ans
