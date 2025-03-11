class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ma, mb, mc = -1, -1, -1
        al, bl, cl = [],[],[]
        for i, c in enumerate(s):
            if c == 'a':
                ma = i
            elif c == 'b':
                mb = i
            else:
                mc = i
            al.append(ma)
            bl.append(mb)
            cl.append(mc)
        ans = 0
        for i in range(len(s)):
            # Have seen all chars
            if al[i] != -1 and bl[i] != -1 and cl[i] != -1:
                cand = min(al[i], bl[i], cl[i])
                ans += 1 + cand # Add all the substrings that end here
        return ans
