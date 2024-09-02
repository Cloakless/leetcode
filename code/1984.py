class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)
        k = k % tot
        i = 0
        while k >= 0:
            k -= chalk[i]
            if k < 0:
                return i
            i += 1
        
