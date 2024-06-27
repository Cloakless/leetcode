class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e,f=edges[0],edges[1]
        return e[0]if e[0]==f[0]or e[0]==f[1]else e[1]
