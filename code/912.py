class Solution:
    from collections import deque
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(lst):
            n = len(lst)
            if n == 0 or n == 1:
                return lst
            a = deque(merge_sort(lst[:n//2]))
            b = deque(merge_sort(lst[n//2:]))
            new_lst = deque()
            while a or b:
                if a and b:
                    if a[0] <= b[0]:
                        val = a.popleft()
                    else:
                        val = b.popleft()
                    new_lst.append(val)
                else:
                    if a:
                        while a:
                            val = a.popleft()
                            new_lst.append(val)
                    else:
                        while b:
                            val = b.popleft()
                            new_lst.append(val)
            return list(new_lst)
        return merge_sort(nums)
