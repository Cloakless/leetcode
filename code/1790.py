class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m != n:
            return False
        if s1 == s2:
            return True
        diff, idxs = 0, []
        for i in range(m):
            if s1[i] != s2[i]:
                diff += 1
                idxs.append(i)
        print(diff)
        if diff != 2 or s1[idxs[0]] != s2[idxs[1]] or s2[idxs[0]] != s1[idxs[1]]:
            return False
        return True
