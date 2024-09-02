class Solution:
    # DSU implementation taken from user "wLui"
    class DSU:
        def __init__(self, n):
            self._parents = list(range(n))
            self._ranks = [0] * n
            return

        def copy(self): # deep copy of a DSU
            other = Solution.DSU(len(self._parents))
            other._parents = self._parents.copy()
            other._ranks = self._ranks.copy()
            return other


        def find(self, u):
            while self._parents[u] != u:
                u = self._parents[u]

            return u


        def connect(self, u, v):
            """
            Return True if u, v already have a shared parent and weren't actually linked
            False otherwise AND connect u, v as needed.
            """
            u_par, v_par = self.find(u), self.find(v)
            if u_par == v_par:
                return True

            # connect them
            if self._ranks[u_par] <= self._ranks[v_par]: # depth of u_par lte that of v_par so connect shorter to deeper
                self._parents[u_par] = v_par
                if self._ranks[u_par] == self._ranks[v_par]: # same size merge results in new parent growing by 1
                    self._ranks[v_par] += 1
            else:
                self._parents[v_par] = u_par

            return False

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ones, twos, threes = [], [], []
        for edge in edges:
            if edge[0] == 1:
                # DSU uses 0-indexing
                ones.append((edge[1]-1, edge[2]-1))
            elif edge[0] == 2:
                twos.append((edge[1]-1, edge[2]-1))
            else:
                threes.append((edge[1]-1, edge[2]-1))
        num_ones, num_twos, num_threes = len(ones), len(twos), len(threes)
        threes_used = 0
        dsu = Solution.DSU(n)
        for edge in threes:
            is_wasted = dsu.connect(edge[0], edge[1])
            if not is_wasted:
                threes_used += 1
        if threes_used == n - 1:
            return num_ones + num_twos + num_threes - (n - 1)
        # 3s not good enough, time to connect more
        alice_dsu = dsu.copy()
        bob_dsu = dsu.copy()
        ones_used, twos_used = 0, 0
        for edge in ones:
            is_wasted = alice_dsu.connect(edge[0], edge[1])
            if not is_wasted:
                ones_used += 1
        if ones_used + threes_used != n - 1:
            # Can't connect up for Alice
            return -1
        for edge in twos:
            is_wasted = bob_dsu.connect(edge[0], edge[1])
            if not is_wasted:
                twos_used += 1
        if twos_used + threes_used != n - 1:
            # Can't connect up for Bob
            return -1
        return num_ones - ones_used + num_twos - twos_used + num_threes - threes_used
