class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        stronk = set()
        for i in range(n):
            stronk.add(i)
        for big, smol in edges:
            if smol in stronk:
                stronk.remove(smol)
        return -1 if len(stronk) > 1 else stronk.pop()
