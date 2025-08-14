class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                cand = int(num[i])
                best = max(best, cand)
        return "" if best == -1 else str(best)*3
