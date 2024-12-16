class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        acc = 0
        class_heap = []
        for pass_i, tot_i in classes:
            if pass_i == tot_i:
                acc += 1
            else:
                heappush(class_heap, (pass_i/tot_i - (pass_i+1)/(tot_i+1), tot_i, pass_i))

        if not class_heap:
            return 1

        for _ in range(extraStudents):
            (rat, tot_i, pass_i) = heappop(class_heap)
            tot_i += 1
            pass_i += 1
            heappush(class_heap, (pass_i/tot_i - (pass_i+1)/(tot_i+1), tot_i, pass_i))
        while class_heap:
            rat, tot_i, pass_i = heappop(class_heap)
            acc += pass_i/tot_i
        return acc / n
