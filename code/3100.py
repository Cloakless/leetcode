class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        while numBottles > 0:
            if numBottles >= numExchange:
                numBottles -= numExchange
                drunk += numExchange
                numExchange += 1
                numBottles += 1
            else:
                drunk += numBottles
                numBottles = 0
        return drunk
