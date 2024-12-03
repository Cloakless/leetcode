class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(1000000)
        next_idx = 0
        ans = ''
        for i in range(len(s)):
            if i == spaces[next_idx]:
                ans += ' '
                next_idx += 1
            ans += s[i]
        return ans
