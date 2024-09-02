class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(s):
            return s == s[::-1]
        
        def parts(st):
            if not st:
                return [[]]
            ans = []
            for i in range(1, len(st) + 1):
                if is_pal(st[:i]):
                    for rest in parts(st[i:]):
                        ans.append([st[:i]] + rest)
            return ans
        
        return parts(s)
