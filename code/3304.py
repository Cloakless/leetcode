class Solution:
    def kthCharacter(self, k: int) -> str:
        n = 1
        word = 'a'
        while n < k:
            for i in range(n):
                new = ord(word[i])+1
                if new > ord('z'):
                    new -= 26
                word += chr(new)
            n *= 2
        return word[k-1]
