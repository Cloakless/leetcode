class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        temp = words + words + words
        aa = -1
        bb = -1
        for i in range(n):
            # print(i)
            if temp[n+startIndex+i] == target:
                aa == i
                return i
            if temp[n+startIndex-i] == target:
                bb == i
                return i
        if aa > 0:
            return aa
        elif bb > 0:
            return bb
        else:
            return -1
