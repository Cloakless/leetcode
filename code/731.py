class MyCalendarTwo:
    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        MAX_BOOKINGS = 2
        clashes = []
        new_start = False
        new_end = False
        curr_num = len(self.events)
        if curr_num == 0:
            new_start = True
            new_end = True
            start_val = 1
            end_val = 0
        # Start is before the first
        if curr_num != 0 and start < self.events[0][0]:
            new_start = True
            start_val = 1
        # Start is after the last
        if curr_num != 0 and start > self.events[curr_num-1][0]:
            new_start = True
            start_val = 1
        # End is before the first
        if curr_num != 0 and end < self.events[0][0]:
            new_end = True
            end_val = 0
        # End is after the last
        if curr_num != 0 and end > self.events[curr_num-1][0]:
            new_end = True
            end_val = 0
        for i in range(curr_num):
            # Might clash
            if self.events[i][0] >= start and self.events[i][0] < end:
                if self.events[i][1] == MAX_BOOKINGS:
                    return False
                clashes.append(i)
            # Is the start a new val
            if i < curr_num - 1:
                if self.events[i][0] < start and self.events[i+1][0] > start:
                    new_start = True
                    if self.events[i][1] == MAX_BOOKINGS:
                        return False
                    start_val = self.events[i][1] + 1
            # Is the end a new val
            if i < curr_num - 1:
                if self.events[i][0] < end and self.events[i+1][0] > end:
                    new_end = True
                    end_val = self.events[i][1]

        for clash in clashes:
            self.events[clash][1] += 1
        if new_start:
            self.events.append([start, start_val])
        if new_end:
            self.events.append([end, end_val])
        self.events.sort()
        return True
