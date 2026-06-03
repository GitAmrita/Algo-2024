from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_level = dict()
        final_lev = defaultdict(list)
        res = []
        if not root:
            return []
        q = deque()
        q.append(root)
        level = 0
        node_level[root] = level
        final_lev[level].append(root.val)
        while q:
            curr = q.popleft()
            level = node_level[curr] + 1
            if curr.left:
                q.append(curr.left)
                node_level[curr.left] = level
                final_lev[level].append(curr.left.val)
            if curr.right:
                q.append(curr.right)
                node_level[curr.right] = level
                final_lev[level].append(curr.right.val)
        for val in final_lev.values():
            res.append(val)
        return res

        