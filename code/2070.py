class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        results = {}
        for price, beauty in items:
            if price not in results:
                results[price] = beauty
            else:
                results[price] = max(results[price], beauty)
        results_lst = sorted([(result, results[result]) for result in results])
        best_result = []
        best = 0
        for result in results_lst:
            best = max(best, result[1])
            best_result.append((result[0], best))
        n = len(best_result)

        def find_best(k):
            if best_result[0][0] > k:
                return 0
            if best_result[n-1][0] <= k:
                return best_result[n-1][1]
            lower = 0
            upper = n - 1

            while lower + 1 < upper:
                mid = (lower + upper) // 2
                if best_result[mid][0] > k:
                    upper = mid
                else:
                    lower = mid
            if best_result[upper][0] <= k:
                return best_result[upper][1]
            else:
                return best_result[lower][1]

        return [find_best(query) for query in queries]
