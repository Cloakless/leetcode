class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            cand = [0]*(i+2)
            for j in range(len(cand)-1):
                cand[j] += ans[-1][j]
                cand[j+1] += ans[-1][j]
            ans.append(cand)
        return ans
