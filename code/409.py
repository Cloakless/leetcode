class Solution:
    def longestPalindrome(self, s: str) -> int:
        tot = 0
        counter = {}
        for letter in s:
            if letter not in counter:
                counter[letter] = 1
            elif counter[letter] == 1:
                counter[letter] = 0
                tot += 2
            else:
                counter[letter] += 1
        for count in counter:
            if counter[count] == 1:
                tot += 1
                return tot
        return tot
