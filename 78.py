class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tot = sets = []
        n = len(nums)
        for i in range(2**n):
            subset = []
            curr = 0
            bin_strin =  str(bin(i)[2:])[::-1]
            digs = len(bin_strin)
            while digs < n:
                bin_strin += '0'
                digs += 1

            for index, digit in enumerate(bin_strin):
                if digit == '1':
                    subset.append(nums[index])
            sets.append(subset)
        return sets
