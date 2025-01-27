class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        deps = defaultdict(set)
        for req in prerequisites:
            a, b = req
            deps[a].add(b)

        @cache
        def precedes(a, b):
            if b in deps[a]:
                return True
            if not deps[a]:
                return False
            ans = False
            for dep in deps[a]:
                ans = (ans or precedes(dep, b))
            return ans
        
        answer = []
        for query in queries:
            answer.append(precedes(query[0],query[1]))
        return answer
        
