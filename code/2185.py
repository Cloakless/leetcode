class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def is_pref(a, b):
            if len(b) < len(a):
                return False
            return all([a[i] == b[i] for i in range(len(a))])
        return sum([int(is_pref(pref, word)) for word in words])
