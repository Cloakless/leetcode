class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        new_box = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_box[i][j] = box[n-1-j][i]

        for j in range(n):
            bot_empty = m - 1
            while new_box[bot_empty][j] != '.' and bot_empty > 0:
                bot_empty -= 1
            faller = bot_empty
            while faller > 0:
                faller -= 1
                if new_box[faller][j] == '#':
                    new_box[faller][j], new_box[bot_empty][j] = new_box[bot_empty][j], new_box[faller][j]
                    bot_empty -= 1
                elif new_box[faller][j] == '*':
                    bot_empty = faller
                    while new_box[bot_empty][j] != '.' and bot_empty > 0:
                        bot_empty -= 1
                        faller = bot_empty
        return new_box
                    
                    

        
        
