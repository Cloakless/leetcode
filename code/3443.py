class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counter = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        best = 0
        for c in s:
            counter[c] += 1
            changes = k
            n, s, e, w = counter['N'], counter['S'], counter['E'], counter['W']
            if n >= s:
                dn = min(changes, s)
                s -= dn
                n += dn
                changes -= dn
            else:
                ds = min(changes, n)
                n -= ds
                s += ds
                changes -= ds
            if e >= w:
                de = min(changes, w)
                w -= de
                e += de
                changes -= de
            else:
                dw = min(changes, e)
                e -= dw
                w += dw
                changes -= dw
            dist = abs(n - s) + abs(e - w)
            best = max(best, dist)
        return best
        
