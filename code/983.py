class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        required = set(days)

        @cache
        def min_cost(day):
            # nonlocal costs
            if day > days[-1]:
                return 0
            if day not in required:
                return min_cost(day+1)
            buy_one = costs[0] + min_cost(day+1)
            buy_seven = costs[1] + min_cost(day+7)
            buy_thirty = costs[2] + min_cost(day+30)
            return min(buy_one, buy_seven, buy_thirty)
        
        return min_cost(days[0])

        
