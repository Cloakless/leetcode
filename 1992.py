class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def find_bounds(farm):
            return [min(square[0] for square in farm), min(square[1] for square in farm), max(square[0] for square in farm), max(square[1] for square in farm)]
        farms = []

        # Essentially a copy of #200
        m = len(land)
        n = len(land[0])

        def complete_island(i,j):
            checked = set()
            new = set()
            new.add((i,j))
            while bool(new):
                point = new.pop()
                checked.add(point)
                point_x = point[0]
                point_y = point[1]
                for p in range(max(point_x-1, 0), min(point_x+2, m)):
                    for q in range(max(point_y-1, 0), min(point_y+2, n)):
                        if land[p][q] == 1 and (point_x-p)*(point_y-q) == 0 and (point_x != p or point_y != q):
                            if (p,q) not in checked:
                                new.add((p,q))
            return checked

        num_islands = 0
        for x in range(m):
            for y in range(n):
                if land[x][y] == 1:
                    num_islands += 1
                    island = complete_island(x,y)

                    farms.append(find_bounds(island))
                    # Wipe everything in this island
                    for point in island:
                        land[point[0]][point[1]] = 0
        return farms
