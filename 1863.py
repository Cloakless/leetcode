class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0
        n = len(nums)
        for i in range(2**n):
            curr = 0
            bin_strin =  str(bin(i)[2:])[::-1]
            digs = len(bin_strin)
            while digs < n:
                bin_strin += '0'
                digs += 1

            for index, digit in enumerate(bin_strin):
                if digit == '1':
                    curr ^= nums[index]
            tot += curr
        return tot
