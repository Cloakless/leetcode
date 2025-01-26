class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        favourite = favorite
        n = len(favourite)
        revs = defaultdict(list)
        for i in range(n):
            revs[favourite[i]].append(i)

        visited = set()

        def search(node, root):
            best = 1
            visited.add(node)
            for rev in revs[node]:
                if rev != root:
                    best = max(best, search(rev, node) + 1)
            return best

        long_cycle = 0
        best_twos = 0
        for i in range(n):
            if i not in visited:
                step = 0
                order = {}
                order[i] = step
                cycle_set = {i}
                pointer = i
                while favourite[pointer] not in cycle_set:
                    visited.add(pointer)
                    step += 1
                    pointer = favourite[pointer]
                    cycle_set.add(pointer)
                    order[pointer] = step
                link = favourite[pointer]

                if pointer == favourite[link]:
                    # Len two cycle
                    l_len = search(link, pointer)
                    r_len = search(pointer, link)
                    best_twos += l_len + r_len
                else:
                    cyc_len = step + 1 - (order[link])
                    long_cycle = max(long_cycle, cyc_len)

        return max(long_cycle, best_twos)    
