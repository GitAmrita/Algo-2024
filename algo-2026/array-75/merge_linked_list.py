# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            merged_head = list1
            list1 = list1.next
        else:
            merged_head = list2
            list2 = list2.next
        merged = merged_head
        while list1 and list2:
          if list1.val <= list2.val:
            merged.next = list1
            list1 = list1.next
            merged = merged.next
          else:
            merged.next = list2
            list2 =list2.next
            merged = merged.next
        if not list1:
            merged.next = list2
        if not list2:
            merged.next = list1
        return merged_head