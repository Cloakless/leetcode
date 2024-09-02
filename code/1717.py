class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def score(st):
            ans = 0
            p, q = x, y
            if q > p:
                p, q = q, p
                st = st[::-1]
            num_as = 0
            num_bs = 0
            length = len(st)
            for char in st:
                if char == 'a':
                    num_as += 1
                if char == 'b':
                    if num_as > 0:
                        num_as -= 1
                        ans += p
                    else:
                        num_bs += 1
            ans += min(num_as, num_bs) * q
            return ans

        tot = 0
        index = 0
        n = len(s)
        indices = []
        subs = []
        for i in range(n):
            if s[i] not in ('a', 'b'):
                indices.append(i)
        first = 0
        for point in indices:
            if first < point:
                subs.append(s[first:point])
            first = point + 1
        subs.append(s[first:])
        for sub in subs:
            tot += score(sub)
        return tot
