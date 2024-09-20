class Solution:
    def shortestPalindrome(self, s: str) -> str:      
        start = ''
        n = len(s)
        for i in range(n+1):
            if start + s == (start + s)[::-1]:
                return start + s
            i += 1
            start += s[n-i]
