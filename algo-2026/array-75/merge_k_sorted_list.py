# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        index = 0
        merged_head = None
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                item = (curr.val, index, curr)
                heapq.heappush(heap, item)
                index += 1
                curr = curr.next
        if not heap:
            return None
        merged_head = heapq.heappop(heap)[2]
        merged = merged_head
        while len(heap) > 0:
            merged.next = heapq.heappop(heap)[2]
            merged = merged.next
        merged.next = None
        return merged_head