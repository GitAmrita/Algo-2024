# You are given an array of meeting time intervals where each interval is represented as: [start_i, end_i]. Determine if a person could attend all meetings.

from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # [[2,4],[7,10]]
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i-1][0] == intervals[i][0]:
            return False
        elif intervals[i-1][1] > intervals[i][0]:
            return False
    return True