class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(key=lambda a: -1*a)
        processorTime.sort()
        worst = 0
        for i, task in enumerate(tasks):
            worst = max(worst, task + processorTime[i//4])
        return worst
