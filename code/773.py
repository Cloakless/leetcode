class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if board == [[1,2,3],[4,5,0]]:
            return 0
        neighbours = set()
        a,b,c,d,e,f = board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2]
        neighbours.add((a,b,c,d,e,f))
        steps = -1
        seen = set()
        while bool(neighbours):
            steps += 1
            new_set = set()
            for neighbour in neighbours:
                if neighbour == (1,2,3,4,5,0):
                    return steps
                seen.add(neighbour)
                a,b,c,d,e,f = neighbour
                if a == 0:
                    opt = (b,a,c,d,e,f)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (d,b,c,a,e,f)
                    if opt not in seen:
                        new_set.add(opt)
                elif b == 0:
                    opt = (b,a,c,d,e,f)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,c,b,d,e,f)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,e,c,d,b,f)
                    if opt not in seen:
                        new_set.add(opt)
                elif c == 0:
                    opt = (a,c,b,d,e,f)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,b,f,d,e,c)
                    if opt not in seen:
                        new_set.add(opt)
                elif d == 0:
                    opt = (d,b,c,a,e,f)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,b,c,e,d,f)
                    if opt not in seen:
                        new_set.add(opt)
                elif e == 0:
                    opt = (a,b,c,e,d,f)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,b,c,d,f,e)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,e,c,d,b,f)
                    if opt not in seen:
                        new_set.add(opt)
                elif f == 0:
                    opt = (a,b,c,d,f,e)
                    if opt not in seen:
                        new_set.add(opt)
                    opt = (a,b,f,d,e,c)
                    if opt not in seen:
                        new_set.add(opt)
            neighbours = new_set
        return -1
