class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e,f=edges[0],edges[1]
        return e[0]if e[0]in f else e[1]
