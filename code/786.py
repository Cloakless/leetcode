class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        decs = []
        ddict = {}
        for first in arr:
            for second in arr:
                if first < second:
                    division = first/second
                    decs.append(division)
                    ddict[division] = (first, second)
        decs.sort()
        return [ddict[decs[k-1]][0],ddict[decs[k-1]][1]]
