class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        k = 1
        while k < n:
            cand = uglies[-1] * 2
            for ugly in uglies:
                if ugly * 5 < cand and ugly * 5 > uglies[-1]:
                    cand = ugly * 5
                if ugly * 3 < cand and ugly * 3 > uglies[-1]:
                    cand = ugly * 3
                if ugly * 2 < cand and ugly * 2 > uglies[-1]:
                    cand = ugly * 2
            uglies.append(cand)
            k += 1
        return uglies[-1]        
