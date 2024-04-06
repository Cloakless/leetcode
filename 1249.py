class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        count = 0
        for char in s:
            if char == "(":
                count += 1
                ans.append(char)
            elif char != ")":
                ans.append(char)
            else:
                if count > 0:
                    count -= 1
                    ans.append(char)
        string = "".join(ans)[::-1]
        ans = []
        count = 0
        for char in string:
            if char == ")":
                count += 1
                ans.append(char)
            elif char != "(":
                ans.append(char)
            else:
                if count > 0:
                    count -= 1
                    ans.append(char)
        return "".join(ans)[::-1]
