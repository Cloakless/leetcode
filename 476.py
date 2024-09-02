class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(math.floor(math.log(num,2)) + 1) - 1 - num
