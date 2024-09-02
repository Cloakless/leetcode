class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        curr_best = 0
        best = max(score)
        print(best)
        n = len(score)
        for i in range(n):
            if score[i] == best:
                print(i)
                score[i] = -1
        print(score)
        if n > 1:
            second = max(score)
            for i in range(n):
                if score[i] == second:
                    score[i] = -2
        if n > 2:
            third = max(score)
            for i in range(n):
                if score[i] == third:
                    score[i] = -3
        if n > 3:
            for i in range(3, n):
                place = i+1
                new_top = max(score)
                for j in range(n):
                    if score[j] == new_top:
                        score[j] = -1 * place
        print(score)
        for k in range(n):
            if score[k] < 0:
                if score[k] == -1:
                    score[k] = "Gold Medal"
                elif score[k] == -2:
                    score[k] = "Silver Medal"
                elif score[k] == -3:
                    score[k] = "Bronze Medal"
                else:
                    score[k] = str(score[k]*-1)
        return score
