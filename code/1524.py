class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        acc = 0
        num_even = 1 # Empty array
        num_odd = 0
        tot = 0
        for num in arr:
            acc += num
            if acc % 2 == 0:
                tot += num_odd
                num_even += 1
            else:
                tot += num_even
                num_odd += 1
        return tot % 1000000007
