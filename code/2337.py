class Solution:
    def canChange(self, start: str, target: str) -> bool:
        m = len(start)
        i, j = 0, 0
        while i < m or j < m:
            while i < m and start[i] == '_':
                i += 1
            while j < m and target[j] == '_':
                j += 1
            if i == m or j == m:
                return i == m and j == m
            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True
