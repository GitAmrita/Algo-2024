# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    added = False
    for s, e in intervals:
        if e < newInterval[0]:
            result.append([s, e])
        elif s > newInterval[1]:
            if not added:
                added = True
                result.append(newInterval)
            result.append([s, e])
        else:
            newInterval[0] = min(s, newInterval[0])
            newInterval[1] = max(e, newInterval[1])
    if not added:
        result.append(newInterval)
    return result