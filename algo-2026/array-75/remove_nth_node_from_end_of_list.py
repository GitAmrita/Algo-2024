# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        helper = []
        curr = head
        while curr:
            helper.append(curr)
            curr = curr.next
        index_to_remove = len(helper) - n
        if index_to_remove < 0:
            return None
        prev = index_to_remove - 1
        future = index_to_remove + 1
        if prev >= 0 and future < len(helper):
            prev_node = helper[prev]
            future_node = helper[future]
            prev_node.next = future_node
            helper[index_to_remove].next = None
        elif prev < 0:
            head = helper[index_to_remove].next
            helper[index_to_remove].next = None
        else:
            prev_node = helper[prev]
            prev_node.next = None
            helper[index_to_remove].next = None
        return head