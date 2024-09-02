class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def word_freq(word):
            counter = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
            for letter in word:
                counter[letter] += 1
            return counter
        base = word_freq(words[0])
        for i in range(1,len(words)):
            new = word_freq(words[i])
            for letter in base:
                base[letter] = min(base[letter], new[letter])
        ans = []
        for letter in base:
            if base[letter] != 0:
                for i in range(base[letter]):
                    ans.append(letter)
        return ans
