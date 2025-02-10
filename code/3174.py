class Solution:
    def clearDigits(self, s: str) -> str:
        to_del = set()
        for i, c in enumerate(s):
            if c.isdigit():
                to_del.add(i)
                for j in reversed(range(i+1)):
                    if not s[j].isdigit() and j not in to_del:
                        to_del.add(j)
                        break
        ans = ''
        for i, c in enumerate(s):
            if i not in to_del:
                ans += s[i]
        return ans
