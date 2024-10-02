class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cop = sorted(set(arr))
        ranks = {}
        for i, elem in enumerate(cop):
            ranks[elem] = i + 1
        for j in range(len(arr)):
            arr[j] = ranks[arr[j]]
        return arr
