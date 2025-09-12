class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for c in s:
            if c in vowels:
                return True
        return False
