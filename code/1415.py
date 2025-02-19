class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        opts = ['a','b','c']
        def happy_strings(m):
            if m == 1:
                return ['a','b','c']
            else:
                cands = happy_strings(m-1)
                ans = []
                for cand in cands:
                    for opt in opts:
                        if opt != cand[0]:
                            ans.append(opt+cand)
            return ans

        try:
            return sorted(happy_strings(n))[k-1]
        except IndexError:
            return ''
