class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for x in range(len(tickets)):
            if x <= k:
                time += min(tickets[k], tickets[x])
            else:
                time += min(tickets[k]-1, tickets[x])
        return time
