class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        if n > m:
            return False
        idx_1, idx_2 = 0, 0
        while idx_1 < m and idx_2 < n:
            if str1[idx_1] == str2[idx_2] or ((ord(str1[idx_1]) + 1) % 26 == ord(str2[idx_2]) % 26):
                idx_1 += 1
                idx_2 += 1
            else:
                idx_1 += 1
        return idx_2 == n
