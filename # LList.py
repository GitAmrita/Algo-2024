# Definition for a Node.
from typing import Optional


class RandomNode:
    def __init__(self, x: int, next: 'RandomNode' = None, random: 'RandomNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class LinkedListSoln:
    def copyRandomList(self, head: 'Optional[RandomNode]') -> 'Optional[RandomNode]':
        if head is None:
            return None
        node_dict = {}
        orig = head
        cpy = None
        cpy_head = None
        cpy = RandomNode(head.val, None, None)
        node_dict[orig] = cpy
        cpy_head = cpy
        idx = 0
        while orig.next:
            cpy.next = RandomNode(orig.next.val, None, None)
            node_dict[orig.next] = cpy.next
            cpy = cpy.next
            orig = orig.next
        cpy = cpy_head
 
        orig = head
        while orig:
            if not orig.random:
                cpy.random = None
            else:
                cpy.random = node_dict[orig.random]
            orig = orig.next
            cpy = cpy.next
        return cpy_head