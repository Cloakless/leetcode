class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        vals = defaultdict(int)
        for row in matrix:
            if row[0] == 1:
                vals[tuple(row)] += 1
            else:
                vals[tuple([1 ^ x for x in row])] += 1
        return max(vals.values())
