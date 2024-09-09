# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        x_lower, x_upper, y_lower, y_upper = 0, n-1, 0, m-1
        x_pos, y_pos = -1, 0 # Start approaching (0,0) from the West
        direction = 'E'
        curr = head
        dir_vec = {'E': (1,0), 'S': (0,1), 'W': (-1,0), 'N': (0,-1)}
        move = dir_vec[direction]
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        while curr:
            x_pos += move[0]
            y_pos += move[1]
            print(y_pos, x_pos)
            ans[y_pos][x_pos] = curr.val
            curr = curr.next
            # Should we switch direction?
            if direction == 'E' and x_pos == x_upper:
                direction = 'S'
                move = dir_vec[direction]
                y_lower += 1
            elif direction == 'S' and y_pos == y_upper:
                direction = 'W'
                move = dir_vec[direction]
                x_upper -= 1
            elif direction == 'W' and x_pos == x_lower:
                direction = 'N'
                move = dir_vec[direction]
                y_upper -= 1
            elif direction == 'N' and y_pos == y_lower:
                direction = 'E'
                move = dir_vec[direction]
                x_lower += 1
        return ans
