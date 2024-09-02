class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        best = [0] + [1000000 for _ in range(n)]
        books = [[0, 0]] + books
        for i in range(1, n + 1):
            w, h = books[i]
            j = i
            # Pull books from the previous shelf
            while w <= shelfWidth and j > 0:
                best[i] = min(best[i], best[j-1] + h)
                j -= 1
                h = max(h, books[j][1])
                w += books[j][0]
        return best[n]
