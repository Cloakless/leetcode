class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        tot_time = 0
        for arrival, time in customers:
            curr_time = max(curr_time + time, arrival + time)
            tot_time += curr_time - arrival
        return tot_time / len(customers)
