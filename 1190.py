class Solution:
    def reverseParentheses(self, s: str) -> str:
        def revString(s):
            n = len(s)
            if n == 0:
                return ""
            if s == "()":
                return ""

            depth = 0
            bases = []
            for i in range(n):
                if s[i] == "(":
                    if depth == 0:
                        bases.append(i)
                    depth += 1
                if s[i] == ")":
                    depth -= 1
                    if depth == 0:
                        bases.append(i)
            if not bases:
                return s
            ans = s[:bases[0]]
            while bases:
                start = bases.pop(0)
                end = bases.pop(0)
                ans += revString(s[start+1:end])[::-1]
                if end < n - 1:
                    if bases:
                        new_star = bases[0]
                    else:
                        new_star = n
                    ans += s[end+1:new_star]
            return ans
        return revString(s)
