class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        n = len(worker)
        jobs = [(0,0)] + sorted(list(zip(difficulty, profit)), key=lambda x: x[0])
        tot, best, i = 0, 0, 0
        for w in worker:
            while i < n + 1 and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            tot += best
        return tot
