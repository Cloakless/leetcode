class Solution:
    def binaryGap(self, n: int) -> int:
        if bin(n).count('1') == 0:
            return 0
        string = bin(n)[2:]
        idxs = []
        for i, val in enumerate(string):
            if val == '1':
                idxs.append(i)
        best = 0
        for j, val in enumerate(idxs):
            if j != 0:
                best = max(best, val - idxs[j-1])
        return best
