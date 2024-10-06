class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        neighbours = []
        heapq.heapify(neighbours)
        heapq.heappush(neighbours, [0, entrance[0], entrance[1]])
        while neighbours:
            dist, x, y = heapq.heappop(neighbours)
            nearest = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
            for a, b in nearest:
                if (a, b) not in visited and 0 <= a and a < m and 0 <= b and b < n and maze[a][b] == '.':
                    if ((a == 0 or a == m-1) or (b == 0 or b == n-1)):
                        return dist + 1
                    visited.add((a, b))
                    heapq.heappush(neighbours, [dist+1, a, b])
        return -1
