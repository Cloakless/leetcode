class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(num, sx, lim):
            nl, sl, tot = len(num), len(sx), 0
            if nl < sl:
                return 0
            elif nl == sl:
                return bool(num >= sx)
            for i in range(nl-sl):
                if lim < int(num[i]):
                    tot += (lim + 1)**(nl-sl-i)
                    return tot
                tot += int(num[i])*(lim+1)**(nl-sl-1-i)

            if num[nl-sl:] >= sx:
                tot += 1
            return tot
        
        return count(str(finish), s, limit) - count(str(start - 1), s, limit)
