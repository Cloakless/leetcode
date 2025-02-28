class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @lru_cache(maxsize=10000)
        def find(a, b):
            if a == '':
                return b
            if b == '':
                return a
            if a[0] == b[0]:
                return a[0] + find(a[1:], b[1:])
            else:
                cand1 = a[0] + find(a[1:], b)
                cand2 = b[0] + find(a, b[1:])
                if len(cand1) > len(cand2):
                    return cand2
                else:
                    return cand1
        
        return find(str1, str2)
