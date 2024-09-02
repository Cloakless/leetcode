class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]

        counter = {}
        for edge in edges:
            if edge[0] not in counter:
                counter[edge[0]] = 1
            else:
                counter[edge[0]] += 1
            if edge[1] not in counter:
                counter[edge[1]] = 1
            else:
                counter[edge[1]] += 1

        while len(edges) > 1:
            # Save off first two in case all edges surround a point
            A = edges[0]
            B = edges[1]
            to_be_removed = set()
            for node in counter:
                if counter[node] == 1:
                    # It's a leaf
                    to_be_removed.add(node)
            new_edges = []
            for edge in edges:
                if edge[0] not in to_be_removed and edge[1] not in to_be_removed:
                    new_edges.append(edge)
                else:
                    # It's going to be removed
                    counter[edge[0]] -= 1
                    counter[edge[1]] -= 1
                    if counter[edge[0]] == 0:
                        del counter[edge[0]]
                    else:
                        del counter[edge[1]]
            edges = new_edges
        if len(edges) == 1:
            return [edges[0][0], edges[0][1]]
        else:
            if A[0] == B[0]:
                return [A[0]]
            elif A[0] == B[1]:
                return [A[0]]
            else:
                return [A[1]]
        
