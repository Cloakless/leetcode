class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        right = {}
        left = {}
        for i in range(len(s)):
            l = s[i]
            r = t[i]
            if l not in right:
                right[l] = r
            elif right[l] != r:
                return False
            if r not in left:
                left[r] = l
            elif left[r] != l:
                return False
        return True
