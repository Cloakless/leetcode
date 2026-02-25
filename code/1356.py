class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x: bin(x).count('1'))
        return arr
