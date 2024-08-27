class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # # Floyd-Warshall
        # # Setup
        # weights = [[0 for _ in range(n)] for _ in range(n)]
        # for i, edge in enumerate(edges):
        #     weights[edge[0]][edge[1]] = succProb[i]
        #     weights[edge[1]][edge[0]] = succProb[i]
        # for j in range(n):
        #     weights[j][j] = 1
        # # Recurrence
        # for a in range(n):
        #     for b in range(a+1,n):
        #         for c in range(n):
        #             if weights[a][c] * weights[c][b] > weights[a][b]:
        #                 weights[a][b] = weights[a][c] * weights[c][b]
        #                 weights[b][a] = weights[a][c] * weights[c][b]
        # return weights[start_node][end_node]

        # Dijkstra
        best = [0] * n
        neighs = [[] for _ in range(n)]
        # Build adjacencies
        for i, edge in enumerate(edges):
            neighs[edge[1]].append([edge[0], succProb[i]])
            neighs[edge[0]].append([edge[1], succProb[i]])
        visited = set()
        best[start_node] = 1
        options = [[-1, start_node]]
        while options:
            # Look for the most likely node to get to
            prob, option = heappop(options)
            if prob > best[end_node]:
                break
            if option == end_node:
                return best[end_node]
            if option in visited:
                pass
            else:
                # Examine its neighbours update their probabilities
                for neighbour, probability in neighs[option]:
                    if neighbour not in visited and best[neighbour] < best[option] * probability:
                        best[neighbour] = best[option] * probability
                        heappush(options, [-1*best[neighbour], neighbour])
                visited.add(option)
        return best[end_node]
