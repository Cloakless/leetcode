class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Function to order a list
        def topo_sort(n, conditions):
            # Turn conditions into edges
            edges = [[] for _ in range(n)]
            nones = set()
            temps = set()
            perms = set()
            for x, y in conditions:
                edges[x-1].append(y-1)
                nones.add(x-1)
                nones.add(y-1)

            # DFS
            def process(m):
                if m in perms:
                    return
                if m in temps:
                    assert False
                temps.add(m)
                for child in edges[m]:
                    process(child)
                perms.add(m)
                nodes.append(m)

            # Process nodes
            nodes = []
            while nones:
                node = nones.pop()
                process(node)

            # Pad if necessary
            for x in range(k):
                if x not in perms:
                    nodes.append(x)
            # Return list
            return nodes[::-1]

        # Order both lists
        try:
            rows = topo_sort(k, rowConditions)
            cols = topo_sort(k, colConditions)
        except AssertionError:
            return []

        # Create matrix directly
        row_vals = {}
        for i in range(k):
            row_vals[rows[i]] = i
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        for j in range(k):
            val = cols[j]
            x = row_vals[val]
            # Everything so far has been 0-indexed
            matrix[x][j] = val + 1
        print(matrix)
        return matrix
