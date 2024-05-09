class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        happiness.reverse()
        tot = 0
        for i in range(k):
            tot += max(happiness[i] - i, 0)
            print(tot)
        return tot
