class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def uglyCount(m):
            singles = [a, b, c]
            doubles = [math.lcm(a,b), math.lcm(c,b), math.lcm(a,c)]
            triples = [math.lcm(a,b,c)]
            tot = 0
            for single in singles:
                tot += m // single
            for double in doubles:
                tot -= m // double
            for triple in triples:
                tot += m // triple
            return tot
        lower = 1
        upper = a*b*c
        if uglyCount(lower) == n:
            return lower
        if uglyCount(upper) == n:
            return upper
        while lower + 1 < upper:
            mid = (lower + upper) // 2
            if uglyCount(mid) < n:
                lower = mid
            else:
                upper = mid
        if uglyCount(lower) == n:
            return lower
        else:
            return lower + 1
