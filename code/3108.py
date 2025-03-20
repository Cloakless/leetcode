class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        component = [i for i in range(n)]
        comp_value = {}

        def canon(x):
            cand = x
            updates = [x]
            while component[cand] != cand:
                updates.append(cand)
                cand = component[cand]
            for update in updates:
                component[update] = cand
            return cand

        def connect(x, y):
            a, b = canon(x), canon(y)
            if a != b:
                component[a] = b

        for a, b, weight in edges:
            connect(a, b)

        for a, b, weight in edges:
            comp = canon(a)
            if comp not in comp_value:
                comp_value[comp] = weight
            else:
                comp_value[comp] &= weight


        ans = []

        @cache
        def comp_num(x):
            return canon(x)

        for start, end in query:
            if comp_num(start) != comp_num(end):
                ans.append(-1)
            else:
                ans.append(comp_value[comp_num(start)])

        return ans

        
