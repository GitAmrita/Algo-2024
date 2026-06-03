from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        if not root:
            return root
        q.append(root)
        while q:
           curr = q.popleft()
           print(curr.val)
           temp = curr.left
           curr.left = curr.right
           curr.right = temp
           if curr.left:
            q.append(curr.left)
           if curr.right:
            q.append(curr.right)
        return root