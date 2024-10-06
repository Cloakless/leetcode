class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        n = 0
        pqueue = []
        heapify(pqueue)
        ans = []
        for query in queries:
            dist = abs(query[0]) + abs(query[1])
            if n < k:
                n += 1
                heappush(pqueue, -1*dist)
            else:
                top = -1*heappop(pqueue)
                if dist < top:
                    heappush(pqueue, -1*dist)
                else:
                    heappush(pqueue, -1*top)
            if n < k:
                ans.append(-1)
            else:
                top = heappop(pqueue)
                ans.append(-1*top)
                heappush(pqueue, top)
        return ans
       
