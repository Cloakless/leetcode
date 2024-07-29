class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        tot = 0
        for j in range(n):
            less = 0
            more = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    less += 1
            for k in range(j, n):
                if rating[j] < rating[k]:
                    more += 1
            tot += more * less

            less = 0
            more = 0
            for k in range(j):
                if rating[k] > rating[j]:
                    less += 1
            for i in range(j, n):
                if rating[j] > rating[i]:
                    more += 1
            tot += more * less
                
        return tot
