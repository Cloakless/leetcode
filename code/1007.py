class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        t_flips = 0
        A = tops[0]
        B = bottoms[0]
        for i in range(1, n):
            if tops[i] not in (A, B) and bottoms[i] not in (A, B):
                return -1
        opts = [0] * 4
        for i in range(n):
            if tops[i] != A:
                if bottoms[i] == A:
                    opts[0] += 1
                else:
                    opts[0] += n
            if bottoms[i] != B:
                if tops[i] == B:
                    opts[1] += 1
                else:
                    opts[1] += n
            if tops[i] != B:
                if bottoms[i] == B:
                    opts[2] += 1
                else:
                    opts[2] += n
            if bottoms[i] != A:
                if tops[i] == A:
                    opts[3] += 1
                else:
                    opts[3] += n
        if min(opts) < n:
            return min(opts)
        return -1
