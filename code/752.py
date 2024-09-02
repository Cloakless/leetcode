class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def find_neighs(combination):
            neighs = []
            digits = list(map(int, list(combination)))
            for i in range(4):
                new = digits
                new[i] += 1
                new[i] = new[i] % 10
                if ''.join(map(str, new)) not in distances:
                    neighs.append(''.join(map(str, new)))
                new[i] += 8
                new[i] = new[i] % 10
                if ''.join(map(str, new)) not in distances and ''.join(map(str, new)):
                    neighs.append(''.join(map(str, new)))
                new[i] += 1
                new[i] = new[i] % 10
            return neighs
        
        distances = {"0000": 0}
        current_neighbours = set()
        current_neighbours.add("0000")
        depth = 0
        while bool(current_neighbours):
            new_neighs = set()
            while bool(current_neighbours):
                node = current_neighbours.pop()
                if node == target:
                    return depth
                distances[node] = depth
                news = find_neighs(node)
                for new in news:
                    if new not in deadends and new not in distances:
                        new_neighs.add(new)
            for neigh in new_neighs:
                current_neighbours.add(neigh)

            depth += 1
        return -1
