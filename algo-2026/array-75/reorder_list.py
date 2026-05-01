# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        helper = []
        curr = head
        while curr:
            helper.append(curr)
            curr = curr.next
        left = 0
        right = len(helper) - 1
        while right - left > 1:
            temp = helper[left].next
            helper[left].next = helper[right]
            helper[right - 1].next = helper[right].next
            helper[right].next = temp
            left += 1
            right -= 1