class Solution:
    def numSteps(self, s: str) -> int:
        t = s[::-1]
        t = list(t)
        tot = 0
        while bool(t):
            n = len(t)
            if n == 1:
                if t[0] == '1':
                    t.pop()
                    break
            if t[0] == '0':
                t.pop(0)
                tot += 1
            else:
                n = len(t)
                tot += 1
                carry = True
                i = 0
                while carry:
                    if t[i] == '1':
                        t[i] = '0'
                    else:
                        t[i] = '1'
                        carry = False
                        break
                    i += 1
                    if i == n:
                        t.append('0')
        return tot
