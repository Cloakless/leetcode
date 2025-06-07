class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_c = [''] * n
        best = s[-1]
        stack = [''] * n
        top = -1
        ans = ''
        for i in range(n):
            cand = s[n-i-1]
            if cand < best:
                best = cand
            min_c[n-i-1] = best
        for i in range(n):
            if i < n-1 and s[i] < min_c[i+1]:
                ans += s[i]
            else:
                top += 1
                stack[top] = s[i]
            while top >= 0 and i < n-1 and stack[top] <= min_c[i+1]:
                ans += stack[top]
                top -= 1
        while top >= 0:
            ans += stack[top]
            top -= 1
        return ans
