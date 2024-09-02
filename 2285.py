class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        scores = [0 for i in range(n)]
        for road in roads:
            scores[road[0]] += 1
            scores[road[1]] += 1
        scores.sort()
        tot = 0
        for j in range(n):
            tot += (j+1) * scores[j]
        return tot
