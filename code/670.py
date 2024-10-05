class Solution:
    def maximumSwap(self, num: int) -> int:
        string = str(num)
        lst = list(map(int, list(string)))
        last_index = [0] * 10
        digit_count = [0] * 10
        for i, digit in enumerate(lst):
            digit_count[digit] += 1
            last_index[digit] = i
        top_digit = 9
        while digit_count[top_digit] == 0:
            top_digit -= 1
        for i, digit in enumerate(lst):
            if digit != top_digit:
                first = i
                next_best = 9
                while digit_count[next_best] == 0 or next_best == digit:
                    next_best -= 1
                last = last_index[next_best]
                lst[first], lst[last] = lst[last], lst[first]
                lst = list(map(str, lst))
                return int("".join(lst))
            else:
                digit_count[digit] -= 1
                while digit_count[top_digit] == 0:
                    top_digit -= 1
                    if top_digit == 0:
                        return num
