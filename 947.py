class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        locations = set()
        for stone in stones:
            locations.add((stone[0],stone[1]))
        
        # Wipe a component and return the number of stones in it
        def wipe(stone):
            rows = {stone[0]}
            cols = {stone[1]}
            visited = set()
            size = 0
            edges = set()
            edges.add(stone)
            while edges:
                (x, y) = edges.pop()
                visited.add((x,y))
                locations.remove((x,y))
                rows.add(x)
                cols.add(y)
                size += 1
                for cand in locations:
                    if cand not in visited and (cand[0] in rows or cand[1] in cols):
                        edges.add(cand)
            return size

        num_stones = 0
        num_components = 0
        while locations:
            start = locations.pop()
            locations.add(start)
            comp_size = wipe(start)
            num_stones += comp_size
            num_components += 1

        # Count connected components
        return num_stones - num_components
