class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        import math
        def canTake(k):
            tot = 0
            for rank in ranks:
                tot += math.floor((k // rank)**0.5)
            return tot >= cars

        lower = 0
        upper = ranks[0]*cars*cars
        while lower + 1 < upper:
            mid = (lower + upper) // 2
            if canTake(mid):
                upper = mid
            else:
                lower = mid
        if canTake(lower):
            return lower
        else:
            return upper


        
