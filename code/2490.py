class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for index, char in enumerate(sentence):
            if char == ' ' and sentence[index-1] != sentence[index+1]:
                return False
        return sentence[0] == sentence[-1]
