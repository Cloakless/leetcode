class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "1":
                ones += 1
            else:
                while i+1 < n and s[i+1] == "0":
                    i += 1
                ans += ones
            i += 1
        return ans
