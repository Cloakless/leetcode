class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def log(s):
            #print(s)
            pass

        w = len(word)
        m = len(board)
        n = len(board[0])

        # Try rule out word being in grid
        if w > m * n:
            log("word too long")
            return False
        
        letters = [inner for outer in board for inner in outer]
        lets = {l: letters.count(l) for l in letters}
        w_lets = {l: word.count(l) for l in word}
        for let in w_lets:
            if let not in lets:
                return False
            if w_lets[let] > lets[let]:
                log("too many of {}".format(let))
                return False
        
        if w == 1:
            return True

        log(lets)
        log(w_lets)

        def search(a, b, k):
            log("looking for {} at {} {}".format(word[k], a, b))
            if a < 0 or a == m or b < 0 or b == n:
                return False
            if board[a][b] != word[k]:
                return False
            if k == w - 1:
                return True

            # Blank current cell and look deeper
            temp = board[a][b]
            board[a][b] = "_"
            
            have_found = search(a+1,b,k+1) or search(a-1,b,k+1) or search(a,b+1,k+1) or search(a,b-1,k+1)

            # Unblank
            board[a][b] = temp

            return have_found


        curr_path = []
        for i in range(m):
            for j in range(n):
                if search(i,j,0):
                    return True
        return False
