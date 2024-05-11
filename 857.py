class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        worths = []
        n = len(quality)
        for i in range(n):
            worths.append([wage[i]/quality[i], quality[i], wage[i]])
        worths.sort(key=lambda x: x[0])
        originals = worths[0:k]
        tot_quality = 0
        qualities = []
        for candidate in originals:
            tot_quality += candidate[1]
            heappush(qualities, -1*candidate[1])
        
        tot_pay = tot_quality * originals[k-1][0]

        candidates = worths[k:]
        for candidate in candidates:
            heappush(qualities, -1*candidate[1])
            tot_quality += candidate[1] + heappop(qualities)
            tot_pay = min(tot_pay, tot_quality * candidate[0])
        return tot_pay
        
