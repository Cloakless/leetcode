class Solution:
    def maskPII(self, s: str) -> str:
        chars = set(s)
        if '@' in chars:
            s = s.lower()
            s = s.split('@')
            s = s[0][0] + '*****' + s[0][-1] + '@' + s[1]
            return s
        else:
            s = list(s)
            digits = []
            for char in s:
                if char.isnumeric():
                    digits.append(char)
            offset = len(digits) - 10
            ans = ''
            if offset > 0:
                ans += '+' + '*'*offset + '-'
            ans += '***-***-' + digits[-4] + digits[-3] + digits[-2] + digits[-1]
            return ans
