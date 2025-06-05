class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {}
        def canon(x):
            if x not in rep:
                rep[x] = x
                return x
            else:
                while x != rep[x]:
                    x = rep[x]
                return x

        for i in range(len(s1)):
            a, b = s1[i], s2[i]
            if a > b:
                a, b = b, a
            c, d = canon(a), canon(b)

            if c < d:
                rep[d] = c
            else:
                rep[c] = d

        ans = ''
        for c in baseStr:
            if c not in rep:
                ans += c
            else:
                ans += canon(c)
        return ans
