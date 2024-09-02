class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for (i, value) in enumerate(arr2):
            order[value] = i
        for thing in arr1:
            if thing not in order:
                order[thing] = 1001 + thing
        arr1.sort(key=lambda t: order[t])
        return arr1
