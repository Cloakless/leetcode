class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        all_meetings = []
        ans = 0
        for start, end in meetings:
            all_meetings.append((start, -1))
            all_meetings.append((end, 1))

        all_meetings.append((days + 1, -1))
        all_meetings.sort()
        prev_day = 0
        in_meeting = 0
        for time, opt in all_meetings:
            in_meeting -= opt
            if in_meeting == 1 and opt == -1:
                ans += max(0, time - prev_day - 1)
                in_meeting = True
            elif in_meeting == 0:
                prev_day = time
        return ans


        
