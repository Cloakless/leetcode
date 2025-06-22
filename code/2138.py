class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        cand = ''
        size = 0
        for c in s:
            if size < k:
                cand += c
                size += 1
            else:
                ans.append(cand)
                cand = c
                size = 1
        cand += fill*(k-size)
        ans.append(cand)
        return ans
