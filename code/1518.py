class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk, spare = 0, 0
        while numBottles:
            drunk += numBottles
            spare += numBottles % numExchange
            numBottles = numBottles // numExchange
            if spare >= numExchange:
                spare -= numExchange
                numBottles += 1 
        return drunk
