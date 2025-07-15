class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vs, cs = 0, 0
        for c in word:
            key = ord(c)
            if key < 48 or (key > 57 and key < 65) or (key > 90 and key < 97) or key > 122:
                return False
            if c.lower() in {'a', 'e', 'i', 'o', 'u'}:
                vs += 1
            elif key > 57:
                cs += 1
        return vs > 0 and cs > 0
