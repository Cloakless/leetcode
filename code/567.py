class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = sorted(s1)
        a = len(s1)
        b = len(s2)
        if a > b:
            return False
        for i in range(b - a + 1):
            if sorted(s2[i:i+a]) == c1:
                return True
        return False
