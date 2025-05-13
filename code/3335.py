class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        @cache
        def cAfterT(c, t):
            if ord(c) + t <= ord('z'):
                return 1
            t -= (ord('z') - ord(c))
            c = 'a'
            return cAfterT(c, t) + cAfterT(c, t - 1)



        ans = 0
        for c in s:
            ans += cAfterT(c, t)
        return ans % 1000000007
       
