import heapq
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    heap = []
    intervals.sort(key=lambda x: x[0])
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if heap[0] <= intervals[i][0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)