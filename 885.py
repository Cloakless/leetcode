class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        n = rows * cols
        output = []
        recorded = 0

        def rotate(direction):
            new_dirs = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
            return new_dirs[direction]

        def advance(coords, direction):
            nonlocal recorded
            nonlocal output
            r, c = coords
            if direction == 'u':
                r, c = r - 1, c
            elif direction == 'r':
                r, c = r, c + 1
            elif direction == 'd':
                r, c = r + 1, c
            elif direction == 'l':
                r, c = r, c - 1
            else:
                assert False 
            if (0 <= r < rows) and (0 <= c < cols):
                recorded += 1
                output += [[r, c]]
            return [r, c]

        # Starting setup
        direction = 'r'
        position = [rStart, cStart]
        output += [position]
        recorded += 1
        magnitude = 1
        while recorded < n:
            for i in range(magnitude):
                position = advance(position, direction)
            direction = rotate(direction)
            for j in range(magnitude):
                position = advance(position, direction)
            direction = rotate(direction)
            magnitude += 1
        return output
