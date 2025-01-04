class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firsts = {}
        lasts = {}
        for i, c in enumerate(s):
            if c not in firsts:
                firsts[c] = i
            lasts[c] = i
        ans = 0
        for idx in range(26):
            # This is the first and last of the palindrome
            letter = chr(idx+97)
            if letter in firsts:
                x = firsts[letter]
                y = lasts[letter]
                seen = set()
                for j in range(x+1, y):
                    seen.add(s[j])
                ans += len(seen)
        return ans
