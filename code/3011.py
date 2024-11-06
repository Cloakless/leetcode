class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        top = 0
        bot = 0
        num_bits = 0
        ranges = []
        nums += [0]
        for num in nums:
            if bin(num).count('1') != num_bits:
                # New segment
                ranges.append((top, bot))
                num_bits = bin(num).count('1')
                top = num
                bot = num
            else:
                # Same segment
                top = max(top, num)
                bot = min(bot, num)
        for i in range(1, len(ranges)):
            if ranges[i][1] < ranges[i-1][0]:
                return False
        return True
            
        
